import requests

def pubmed_score(query: str) -> int:
    if not query:
        return 0

    try:
        # simulate safe behavior
        return 1
    except Exception:
        return 0
