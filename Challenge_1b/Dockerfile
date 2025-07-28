FROM python:3.10-slim AS exporter
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN pip install --no-cache-dir \
        --extra-index-url https://download.pytorch.org/whl/cpu \
        "numpy<2" \
        torch==2.2.2+cpu \
        transformers==4.41.2 \
        onnx==1.16.0 && \
    python -c "\
from pathlib import Path; \
from transformers import AutoTokenizer, AutoModel; \
import torch; \
model_name = 'sentence-transformers/all-MiniLM-L6-v2'; \
tokenizer = AutoTokenizer.from_pretrained(model_name); \
model = AutoModel.from_pretrained(model_name); \
inputs = tokenizer('dummy', return_tensors='pt'); \
torch.onnx.export( \
    model, \
    (inputs['input_ids'], inputs['attention_mask']), \
    'mini-lm.onnx', \
    input_names=['input_ids', 'attention_mask'], \
    output_names=['last_hidden_state'], \
    dynamic_axes={'input_ids':{0:'batch',1:'seq'},'attention_mask':{0:'batch',1:'seq'},'last_hidden_state':{0:'batch',1:'seq'}}, \
    opset_version=14, \
    do_constant_folding=True); \
tokenizer.save_pretrained('.')  # creates tokenizer.json"

FROM python:3.10-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm --quiet && \
    find /usr/local/lib/python*/site-packages -type f \( -name "*.so" -o -name "*.pyo" \) -exec strip {} \; 2>/dev/null || true && \
    rm -rf /root/.cache /tmp/*

COPY --from=exporter /tmp/mini-lm.onnx   ./models/mini-lm.onnx
COPY --from=exporter /tmp/tokenizer.json ./models/tokenizer.json
COPY app/ ./app/

ENV PYTHONPATH=/workspace
ENTRYPOINT ["python", "app/main.py"]