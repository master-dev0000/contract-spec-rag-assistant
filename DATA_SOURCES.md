# 📊 Data Sources & Document Corpus: Contract & Specification RAG Assistant

This repository implements an enterprise Retrieval-Augmented Generation (RAG) assistant for complex civil engineering contracts and technical specifications, operating under the **PMI-CPMAI™ (Cognitive Project Management in AI)** governance framework. This document catalog details the official corpora, standard contract forms, and technical specifications ingested into the ChromaDB vector repository.

---

## 1. FIDIC International Standard Conditions of Contract
* **Authoritative Source:** International Federation of Consulting Engineers (FIDIC - *Fédération Internationale Des Ingénieurs-Conseils*)
* **Access Reference:** [FIDIC Bookshop & Standard Contracts](https://fidic.org/books) (Public harmonized clauses available in World Bank Standard Procurement Documents)
* **Document Types:** Multilateral EPC / Turnkey and Design-Build contracts.
* **Corpus Scope:** Unambiguous contract conditions defining risk allocation, payment certification, time extension claims, and dispute escalation.

### Core Contractual Clauses Ingested
* **Clause 4 [The Contractor]:** General obligations, performance security, contractor's superintendence, and quality assurance systems.
* **Clause 8 [Commencement, Delays and Suspension]:** Extension of Time (EOT) for completion, delay damages, and contractor suspension.
* **Clause 13 [Variations and Adjustments]:** Right to vary, variation procedure, value engineering evaluation, and adjustments for changes in legislation.
* **Clause 14 [Contract Price and Payment]:** Advance payment, interim payment applications, Schedule of Payments, and retention money release.
* **Clause 17 [Care of the Works and Indemnities]:** Contractor's liability, indemnities, and consequences of Employer's risks.
* **Clause 20 & 21 [Claims, Disputes and Arbitration]:** Contractor/Employer claims procedure (28-day notice rule), DAAB (Dispute Avoidance/Adjudication Board) constitution and decisions.

---

## 2. World Bank Standard Procurement Documents (SPD) - Works & EPC
* **Authoritative Source:** The World Bank Operations Policy and Country Services
* **Official Access Portal:** [World Bank Standard Bidding Documents](https://www.worldbank.org/en/projects-operations/products-and-services/brief/procurement-standard-bidding-documents)
* **Format:** Unrestricted Public PDF / DOCX
* **Licensing:** Open World Bank Document Repository.
* **Corpus Scope:** Environmental, Social, Health and Safety (ESHS) specifications, bidding procedures, and General Conditions of Contract for major public infrastructure loans.

---

## 3. DNIT - Especificações Técnicas e Manuais de Infraestrutura Rodoviária
* **Authoritative Source:** Departamento Nacional de Infraestrutura de Transportes (DNIT) - Instituto de Pesquisas Rodoviárias (IPR)
* **Official Access Portal:** [Coletânea Oficial de Normas e Manuais do DNIT](https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/coletanea-de-normas)
* **Format:** PDFs normativos de livre acesso público.
* **Licensing:** Domínio Público Federal (Brasil).

### Specific Standards Ingested for Tolerance & Compliance Retrieval
* **DNIT 108/2009 - PRO:** *Terraplenagem - Aterros - Procedimento* (parâmetros de compactação de aterros, ensaios Proctor, tolerâncias geométricas de cota).
* **DNIT 141/2010 - ES:** *Pavimentação asfáltica - Pré-misturado a frio com emulsão catiônica - Especificação de serviço*.
* **DNIT 031/2006 - ES:** *Pavimentos flexíveis - Concreto asfáltico - Especificação de serviço* (faixas granulométricas A, B, C, índice de vazios, estabilidade Marshall).
* **DNIT 085/2006 - EM:** *Tubos de concreto armado para bueiros - Especificação de material*.

---

## 4. ABNT Normas Brasileiras Regulamentadoras (Referência e Validação)
* **Referência:** Associação Brasileira de Normas Técnicas (ABNT)
* **Normas Catalogadas:**
  * **ABNT NBR 6118:2023:** *Projeto de estruturas de concreto - Procedimento* (Fatores de segurança $\gamma_c, \gamma_f, \gamma_s$, classes de agressividade ambiental CAA I a IV, cobrimento nominal mínimo de armaduras).
  * **ABNT NBR 12721:2006:** *Avaliação de custos unitários e preparo de orçamento de construção* (Critérios de rateio de área equivalente, frações ideais e orçamentação CUB/NBR).
  * **ABNT NBR 5674:2012:** *Manutenção de edificações - Requisitos para o sistema de gestão de manutenção*.

---

## Vector Ingestion Pipeline Code Snippet
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_normative_pdf(pdf_path: str, standard_code: str):
    """Loads, chunks, and attaches CPMAI metadata tags to normative engineering specifications."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n## ", "\n### ", "\nArtigo ", "\nClause ", "\n\n", "\n", " "]
    )
    docs = splitter.split_documents(pages)
    for doc in docs:
        doc.metadata["standard_code"] = standard_code
        doc.metadata["source_type"] = "Technical_Specification"
    return docs
```
