from fastapi import FastAPI, Depends
from app.deps import get_tenant_id
from app.schemas import QueryRequest, QueryResponse, Source
from app.ingest import load_docs
from app.store import search, snippet

app = FastAPI(title="Multi-tenant SaaS Test")

STORE = load_docs("data")

@app.get("/health")
def health():
    return {"ok": True, "docs": {k: len(v) for k, v in STORE.items()}}

@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest, tenant_id: str = Depends(get_tenant_id)):
    docs = STORE.get(tenant_id, [])
    hits = search(docs, req.question, top_k=3)

    if not hits:
        return QueryResponse(
            answer=None,
            sources=[],
            no_answer=True,
            reason="No relevant documents for this tenant."
        )

    sources = [Source(filename=h["filename"], snippet=snippet(h["content"])) for h in hits]

    # Only what I found plus source
    answer = "Relevant excerpts:\n" + "\n".join(
        f"- {s.filename}: {s.snippet}" for s in sources
    )

    return QueryResponse(answer=answer, sources=sources, no_answer=False, reason=None)
