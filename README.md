
# 🚀 Adobe India Hackathon 2025 - Document Intelligence Solutions

## 📋 Executive Summary

This repository presents comprehensive solutions for Adobe's Document Intelligence Hackathon 2025, encompassing two distinct challenges focused on advanced PDF processing and persona-driven content analysis. Both implementations adhere to stringent performance requirements including sub-60-second execution times and containerized deployment within 1GB resource constraints.

## 🎯 Challenge Overview

### 📊 Round 1A: Hierarchical Document Structure Extraction
**Objective**: Automated extraction and structuring of document hierarchies from PDF sources  
**Deliverable**: JSON-formatted outline with hierarchical heading classification and precise page references  
**Technical Approach**: Heuristic-based parsing with multi-level heading detection algorithms

### 🧠 Round 1B: Intelligent Content Relevance Analysis  
**Objective**: Context-aware section ranking based on user personas and specific task requirements  
**Deliverable**: Ranked content sections with relevance scoring and detailed subsection analysis  
**Technical Approach**: ONNX-powered semantic embeddings with persona-specific relevance algorithms

## 🏗️ Repository Architecture

### Project Structure
```
📁 Challenge_1a/
│
├── 📁 input/                    # Input PDF files
│   ├── file01.pdf
│   ├── file02.pdf
│   ├── file03.pdf
│   ├── file04.pdf
│   ├── file05.pdf
│   └── multilingual.pdf
│
├── 📁 output/                   # Output structured JSONs
│   ├── file01.json
│   ├── file02.json
│   ├── file03.json
│   ├── file04.json
│   ├── file05.json
│   └── multilingual.json
│
├── 📁 src/                      # Core processing logic
│   ├── __pycache__/
│   ├── __init__.py
│   ├── extractor.py
│   ├── main.py
│   ├── pdf_processor.py
│   └── utils.py
│
├── build_and_run.bat           # Windows batch file to build and run
├── Dockerfile                  # Container setup for Challenge_1a
├── README.md                   # Documentation for Challenge_1a
└── requirements.txt            # Python dependencies

📁 Challenge_1b/                     # Persona-Driven Analysis
│
├── 📁 app/                          # AI processing pipeline
├── 📁 Collection 1/                # Travel planning documents
├── 📁 Collection 2/                # Software tutorial collection
├── 📁 Collection 3/                # Culinary content library
├── Dockerfile                      # Container setup for Challenge_1b
└── Readme.md                       # Documentation for Challenge_1b

```

## 🔧 Implementation Guide

### 🔍 Challenge 1A: Structure Extraction Engine

**Build Process:**
On Windows, simply run the provided batch file:
.\build_and_run.bat

## Using Docker Manually:-
```bash
docker build -t document-structure-analyzer ./Challenge_1a
```

**Execution:**
```bash
docker run --rm 
  -v "$(pwd)/Challenge_1a/input_data:/application/input:ro" 
  -v "$(pwd)/Challenge_1a/output_results:/application/output" 
  --platform linux/amd64 
  document-structure-analyzer
```

**Output Format**: Structured JSON containing hierarchical document elements with classification levels and page coordinates.

### 🎭 Challenge 1B: Persona Intelligence Engine

**Build Process:**
```bash
docker build -t persona-intelligence-system ./Challenge_1b
```

**Execution:**
```bash
docker run --rm 
  -v "$(pwd)/Challenge_1b/Dataset_1:/workspace/input:ro" 
  -v "$(pwd)/Challenge_1b/Dataset_1:/workspace/output" 
  persona-intelligence-system
```

**Output Format**: Comprehensive JSON containing ranked content sections with persona-specific relevance scores and detailed analytical insights.

## ⚙️ Technical Specifications

### 🛠️ Core Technologies and Dependencies

| Technology Stack | Implementation Scope | Functional Purpose |
|------------------|---------------------|-------------------|
| Python 3.10 | Universal Runtime | Primary development platform |
| PyPDF2 Library | Challenge 1A | Document structure parsing |
| PyMuPDF (fitz) | Challenge 1A |Primary PDF parsing and analysis |
| pdfminer.six | Challenge 1A |For detailed text extraction and analysis |
| Pillow  | Challenge 1A |For image processing support|
| PyMuPDF Framework | Challenge 1B | High-performance content extraction |
| ONNX Runtime + MiniLM | Challenge 1B | Semantic embedding generation |
| spaCy + Tokenizers | Challenge 1B | Natural language processing |
| Docker Containerization | Both Challenges | Deployment standardization |

### 📈 Performance Metrics

- **Processing Speed**: Sub-60 second execution guarantee
- **Resource Efficiency**: Maximum 1GB container footprint
- **Scalability**: Multi-document batch processing capability
- **Accuracy**: High-precision content classification and ranking

## ✅ Quality Assurance

### Testing Framework
- Comprehensive unit testing across all processing modules
- Integration testing for complete pipeline validation
- Performance benchmarking against resource constraints
- Cross-platform compatibility verification

### Documentation Standards
- Detailed API documentation for all public interfaces
- Comprehensive deployment guides with troubleshooting
- Performance optimization recommendations
- Maintenance and update procedures


## 👨‍💻 Built With ❤️ by **Team Semicolon** — Adobe India Hackathon 2025

- **Abhinav Tiwari**
- **Rozy Koranga**
 
**Academic Background**: B.Tech (Computer Science and Engineering)  
**Project Classification**: Adobe India Hackathon 2025 Submission
