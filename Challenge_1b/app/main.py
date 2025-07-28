import json, time, sys, os
from pathlib import Path

from pdf_parser import load_pdfs
from ranker import rank_sections

def main():
    t0 = time.time()

    in_file = Path("input/challenge1b_input.json")
    cfg = json.loads(in_file.read_text())

    docs = load_pdfs(Path("input/PDFs"), cfg["documents"])
    print(f"Loaded {len(docs)} PDFs with {sum(len(d.sections) for d in docs)} sections", file=sys.stderr)

    query = f"{cfg['persona']['role']} needs to {cfg['job_to_be_done']['task']}"
    top_sections = rank_sections(docs, query, top_k=10)

    extracted = []
    sub_analysis = []
    for sec in top_sections:
        extracted.append({
            "document": sec.doc_name,
            "section_title": sec.title,
            "importance_rank": sec.rank,
            "page_number": sec.page
        })
        sub_analysis.append({
            "document": sec.doc_name,
            "refined_text": sec.text[:256].strip(),
            "page_number": sec.page
        })

    output = {
        "metadata": {
            "input_documents": [d["filename"] for d in cfg["documents"]],
            "persona": cfg["persona"]["role"],
            "job_to_be_done": cfg["job_to_be_done"]["task"]
        },
        "extracted_sections": extracted,
        "subsection_analysis": sub_analysis
    }

    out_file = Path("output/challenge1b_output.json")
    out_file.parent.mkdir(exist_ok=True)
    out_file.write_text(json.dumps(output, indent=2))

    print(f"Finished in {time.time()-t0:.1f}s", file=sys.stderr)

if __name__ == "__main__":
    main()