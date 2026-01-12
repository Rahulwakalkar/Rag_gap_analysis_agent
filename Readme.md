#  Policy Gap Analysis Agent

A production-ready AI-powered regulatory gap analysis system built using LangGraph, Groq LLM, Streamlit, and FAISS-backed vector search.

The agent compares a regulatory policy document with an internal policy document to identify compliance gaps, assess risk severity, and generate actionable recommendations in a structured, audit-ready format.

---

##  Features

- PDF Upload Support (Regulatory & Internal policies)
-  LLM-based Requirement Extraction (Groq – LLaMA 3)
- Semantic Policy Mapping using embeddings + vector DB
-  Gap Detection & Severity Classification
-  Structured JSON Output(audit & compliance ready)
- Interactive Streamlit UI
- LangGraph Multi-step Agent Architecture
- Deterministic + LLM Hybrid Design (Production Safe)



## 🏗️ Architecture Overview

PDF Documents
│
▼
Document Loader & Chunker
│
▼
Regulatory Requirement Extraction (LLM)
│
▼
Vector Store (FAISS)
│
▼
Policy Mapping (Semantic Search)
│
▼
Gap Detection (Rule-based)
│
▼
Final Report Generation (JSON)

########################################################
Gap_analysis_agent/
├── app/

│ ├── agent/
│ │ ├── graph.py # LangGraph workflow
│ │ ├── state.py # Typed agent state
│ │ ├── nodes/
│ │ │ ├── llm_node.py # Requirement extraction
│ │ │ ├── tool_node.py # Policy mapping (vector DB)
│ │ │ ├── router_node.py # Gap detection & severity
│ │ │ └── fallback_node.py # Final report
│ │
| |
│ ├── services/
│ │ ├── llm.py # Groq LLM wrapper
│ │ ├── embeddings.py # Embedding service
│ │ ├── document_loader.py # PDF parsing & chunking
│ │ └── vectorstore.py # FAISS integration
│ │
| |
│ ├── core/
│ │ ├── config.py # Environment config
│ │ └── logging.py # Structured logging
│
├── streamlit_app.py # Streamlit entrypoint
├── tests/ # Unit & integration tests
├── scripts/ # Utility scripts
├── .env # Environment variables
├── requirements.txt
├── README.md

streamlit run streamlit_app.py
