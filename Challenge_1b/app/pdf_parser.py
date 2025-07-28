import fitz
from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class Section:
    doc_name: str
    page: int
    title: str
    text: str

@dataclass
class Document:
    name: str
    sections: List[Section]

def load_pdfs(pdf_dir: Path, doc_meta: list) -> List[Document]:
    docs = []
    for item in doc_meta:
        path = pdf_dir / item["filename"]
        doc = fitz.open(path)
        sections = []

        for page_idx in range(len(doc)):
            page = doc[page_idx]
            blocks = page.get_text("dict")["blocks"]
            for b in blocks:
                if b["type"] != 0:
                    continue
                for line in b["lines"]:
                    for span in line["spans"]:
                        if span["flags"] & 2**4 and span["size"] >= 14:
                            title = span["text"].strip()
                            sections.append(
                                Section(doc_name=item["filename"],
                                        page=page_idx+1,
                                        title=title,
                                        text="")
                            )
                        else:
                            if sections:
                                sections[-1].text += span["text"] + " "
        if not sections:
            text = "".join(page.get_text() for page in doc)
            sections.append(Section(doc.name, 1, "Full document", text))
        docs.append(Document(item["filename"], sections))
    return docs