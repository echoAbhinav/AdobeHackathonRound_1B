import numpy as np
import onnxruntime as ort
from pathlib import Path
from typing import List
import spacy

sess = ort.InferenceSession("models/mini-lm.onnx",
                            providers=["CPUExecutionProvider"])
nlp = spacy.load("en_core_web_sm")

from tokenizers import Tokenizer
tok = Tokenizer.from_file("/workspace/models/tokenizer.json")

def embed(text: str) -> np.ndarray:
    encoded = tok.encode(text)
    ids = np.array([encoded.ids], dtype=np.int64)
    mask = np.array([encoded.attention_mask], dtype=np.int64)
    ort_inputs = {"input_ids": ids, "attention_mask": mask}
    out = sess.run(None, ort_inputs)[0]            
    mask = mask.astype(np.float32)
    pooled = np.sum(out * mask[..., None], axis=1) / np.sum(mask, axis=1, keepdims=True)
    return pooled.squeeze()

def rank_sections(docs, query: str, top_k: int = 10):
    q_emb = embed(query)
    q_words = {w.lemma_.lower() for w in nlp(query) if w.is_alpha and not w.is_stop}

    scored = []
    for doc in docs:
        for sec in doc.sections:
            if not sec.text.strip():
                continue
            s_emb = embed(sec.title + " " + sec.text[:512])
            cos = float(np.dot(q_emb, s_emb) /
                        (np.linalg.norm(q_emb) * np.linalg.norm(s_emb) + 1e-9))

            s_words = {w.lemma_.lower() for w in nlp(sec.text) if w.is_alpha and not w.is_stop}
            overlap = len(q_words & s_words) / max(1, len(q_words))
            score = 0.8 * cos + 0.2 * overlap

            sec.rank = None
            scored.append((-score, sec))

    top = sorted(scored, key=lambda x: x[0])[:top_k]
    for rank, (_, sec) in enumerate(top, start=1):
        sec.rank = rank
    return [sec for _, sec in top]