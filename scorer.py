def score_lead(row, pubmed_score):
    score = 0

    title = str(row.get("title", "")).lower()
    company = str(row.get("company", "")).lower()

    keywords = ["toxicology", "safety", "hepatic"]

    if any(k in title for k in keywords):
        score += 2

    if any(k in company for k in keywords):
        score += 1

    score += pubmed_score
    return score
