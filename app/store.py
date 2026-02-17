import re
from typing import List, Dict, Tuple

def _tokens(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9]{3,}", text.lower())

def snippet(text: str, n: int = 220) -> str:
    t = " ".join(text.split())
    return t[:n] + ("..." if len(t) > n else "")

def search(docs: List[Dict[str, str]], question: str, top_k: int = 3) -> List[Dict[str, str]]:
    q = set(_tokens(question))
    if not q:
        return []

    scored: List[Tuple[int, Dict[str, str]]] = []
    for d in docs:
        c = d["content"].lower()
        score = sum(1 for tok in q if tok in c)
        if score > 0:
            scored.append((score, d))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:top_k]]
