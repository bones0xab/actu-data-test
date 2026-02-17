# Multi-Tenant RAG SaaS – Technical Demo

## Overview
This project is a **multi-tenant SaaS technical demo** built with **FastAPI** and **Streamlit**.
It demonstrates a **Retrieval-Augmented Generation (RAG) architecture**, with a strong focus on **document retrieval, tenant isolation, and explainability**.

The system is designed with **AI integration readiness**, but the **LLM layer is optional and future-oriented**.
All core features work **fully without any LLM**.

This project is **not a production SaaS**. It is an **architectural and educational demonstration**.

---

## Goals
- Demonstrate clean **multi-tenant isolation**
- Show **deterministic document retrieval**
- Provide **transparent and explainable outputs**
- Prepare the system for **future AI integration** without making it mandatory

---

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Language:** Python
- **Search:** Keyword-based document retrieval
- **Authentication:** API Key (`X-API-KEY`)
- **Testing:** pytest
- **AI (optional / future):** Local LLM integration (Ollama-ready)

> ⚠️ The system works fully **without an LLM**.
> AI is an optional extension, not a runtime dependency.

---

## Architecture

### High-Level Flow

![img_1.png](./screens/workflow.png)

### Key Concepts

#### 1. Tenant Isolation
- Each request includes an `X-API-KEY` header
- The API key is mapped to a tenant identifier
- Each tenant accesses **only its own documents**

#### 2. Per-Tenant Document Loading
- Documents are loaded and stored **per tenant**
- No cross-tenant data access is possible

#### 3. Deterministic Retrieval
- Retrieval is keyword-based and fully deterministic
- Given the same input, results are always the same

#### 4. Optional AI Layer
- An AI reasoning layer can be plugged in **after retrieval**
- AI does **not** search documents
- AI only explains or summarizes retrieved content

#### 5. Separation of Responsibilities
- Retrieval = backend logic
- Generation (AI) = optional explanation layer
- Response formatting = backend controlled

---

## Core Features

### Current Features
- Multi-tenant document isolation
- Manual retrieval testing
- Source traceability
- No-answer detection
- Fully deterministic responses

### Future-Ready Features
- LLM-based explanation layer
- Natural language answers
- Advanced reasoning on top of retrieved content

---

## API Documentation

### `GET /health`
Health check endpoint.

**Response example:**
```json
{
  "ok": true,
  "docs": {
    "A": 4,
    "B": 3
  }
}

```

### `POST /query`

Query documents for a specific tenant.

**Headers:**

```json
{
  "X-API-KEY" : "<tenant-key>",
  "Content-Type": "application/json"
}

```

**Request body:**

```json
{
  "question": "How can I cancel the contract?"
}

```

**Response example (documents found):**

```json
{
  "answer": "The contract can be cancelled within 30 days. ",
  "sources": [
    {
      "filename": "docA1.txt",
      "snippet": "The contract may be cancelled within 30 days..."
    }
  ],
  "no_answer": false,
  "reason": null
}

```

**Response example (no relevant documents):**

```json
{
  "answer": null,
  "sources": [],
  "no_answer": true,
  "reason": "No relevant documents for this tenant."
}

```

---

## Streamlit UI

### Manual Test Panel

* **Displays raw retrieved snippets:** See exactly what data is being pulled from the source.
* **Shows exactly what the system found:** No hidden filters or "magic" transformations.
* **Ensures transparency and traceability:** Every result can be traced back to its origin.

### Why This Matters

* **Helps validate retrieval logic:** Confirm that the system is fetching the *right* documents.
* **Makes debugging easy:** Identify quickly if an issue is in the search logic or the data.
* **Prevents “black box” behavior:** Understanding the *how* builds developer trust.

### AI Comparison Panel (Planned)

* Will show AI-generated explanations side-by-side with raw data.
* **Note:** Not required for current system operation.

---

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt

```

### 2. Run the Backend

```bash
uvicorn app.main:app --reload

```

### 3. Run the Frontend

```bash
streamlit run app.py

```

> [!IMPORTANT]
> **⚠️ Ollama or any LLM is not required to run the project.** The core system functions deterministically.

---

## Folder Structure

```text
app/
├── main.py         # FastAPI entry point and API routes
├── store.py        # Document search and retrieval logic
├── ingest.py       # Document loading per tenant
├── schemas.py      # Pydantic request/response models
├── deps.py         # Tenant resolution via API key
├── app.py          # Streamlit UI
└── ollama_agent.py # Future AI extension (optional)

```

---

## Design Decisions

### Why Deterministic Retrieval

* **Predictable behavior:** The same query always returns the same result.
* **Easy to test:** Simplifies unit testing and QA.
* **Easy to explain and debug:** Clear logic path for developers.

### Why AI Is Optional

* Core system must be reliable and functional without external LLM dependencies.
* AI adds value (summarization) but should not replace core data retrieval logic.

### Why Explainability First

* Users and developers must trust results; seeing raw sources builds that trust.
* Raw sources are always visible to the end-user.

### Why Backend Controls Sources

* Prevents "hallucinated" citations by the LLM.
* Ensures traceability and keeps responses fully auditable for compliance.

---

## Project Scope

### 🚩 Limitations

* No vector database (uses keyword/deterministic search).
* No real authentication provider (uses API keys for tenant resolution).
* No async background jobs.
* AI layer not enabled by default.

### 🚀 Future Improvements

* Enable AI explanation layer (Ollama integration).
* Switch to vector-based retrieval for semantic search.
* Add streaming responses for better UI/UX.
* Introduce async processing for high-concurrency.
* Implement Role-Based Access Control (RBAC).

---

## Summary

This project demonstrates a clean, explainable, and extensible RAG (Retrieval-Augmented Generation) architecture with:

1. **Strong separation of concerns** (FastAPI backend vs. Streamlit frontend).
2. **Deterministic core logic** for reliability.
3. **Optional intelligence layer** for future-proofing.

It prioritizes **clarity, correctness, and future readiness** over unnecessary complexity.

```

```
