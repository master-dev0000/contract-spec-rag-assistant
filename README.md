# Contract & Technical Specification Compliance Assistant
### Enterprise RAG Architecture under PMI-CPMAI™ Governance

[![LangChain](https://img.shields.io/badge/RAG-LangChain-1C3C3C.svg)](https://www.langchain.com/)
[![VectorDB: Chroma](https://img.shields.io/badge/VectorDB-ChromaDB-blue.svg)](https://www.trychroma.com/)
[![Governance: PMI--CPMAI](https://img.shields.io/badge/Governance-PMI--CPMAI™-purple.svg)](#)
[![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io/)

An executive GenAI compliance assistant designed to ingest hundreds of pages of engineering specifications (ABNT NBR, Eurocodes, ASTM) and complex EPC (Engineering, Procurement, Construction) contractual clauses, answering technical queries with strict citation auditing.

```mermaid
flowchart TD
    A["ABNT / Eurocodes Norms & EPC Contract PDFs"] --> B["Document Chunking & Metadata Injection"]
    B --> C["Vector Embeddings (ChromaDB Vector Store)"]
    D["User Technical Query"] --> E["Similarity Search & Context Retrieval"]
    C --> E
    E --> F["Audited Prompt Formulation (Strict Anti-Hallucination)"]
    F --> G["LLM Response with Exact Clause & Article Citation"]
```

## Governance & PMI-CPMAI™ Compliance
Built in direct accordance with the **PMI-CPMAI™ (Cognitive Project Management in AI)** framework:
- **Domain I (Responsible AI):** Deterministic audit trail referencing exact norm standard, article number, and page citation.
- **Domain II (Business Viability):** Reduces technical contract verification time from 40 hours to under 30 minutes.
- **Domain III (Data Quality):** Strict chunking strategy preventing semantic drift across technical tolerances and safety factors.

## Quickstart
```bash
git clone https://github.com/master-dev0000/contract-spec-rag-assistant.git
cd contract-spec-rag-assistant
pip install -r requirements.txt
streamlit run app/app.py
```

## License
MIT License. Developed by André Belarmino Alves.
