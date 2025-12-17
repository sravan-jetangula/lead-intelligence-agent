from Bio import Entrez

Entrez.email = "demo@example.com"

def pubmed_score(company):
    try:
        handle = Entrez.esearch(
            db="pubmed",
            term=company,
            retmax=5
        )
        record = Entrez.read(handle)
        return len(record.get("IdList", []))
    except Exception:
        return 0
