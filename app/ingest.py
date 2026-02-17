from pathlib import Path

ALLOWED_EXT = {".txt", ".md"}

def load_docs(data_dir: str = "data") -> dict:
    base = Path(data_dir)
    store = {"A": [], "B": []}

    mapping = {"A": "tenantA", "B": "tenantB"}
    for tenant_id, folder in mapping.items():
        p = base / folder
        if not p.exists():
            continue

        for fp in p.glob("*"):
            if fp.is_file() and fp.suffix.lower() in ALLOWED_EXT:
                store[tenant_id].append({
                    "filename": fp.name,
                    "content": fp.read_text(encoding="utf-8", errors="ignore"),
                })
    return store
