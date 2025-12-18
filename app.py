import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------
# Page config (MUST be first)
# -------------------------------
st.set_page_config(
    page_title="Lead Intelligence Agent",
    layout="wide"
)

# -------------------------------
# Title & Description
# -------------------------------
st.title("🔍 Lead Intelligence Agent")

st.markdown(
    """
    This interactive dashboard analyzes professional profiles from the life-sciences domain 
    and assigns relevance scores based on role keywords and research focus.  
    The goal is to surface and prioritize potential collaborators or leads who are most 
    aligned with advanced **3D in-vitro, safety, and toxicology-driven research workflows**.
    """
)

# -------------------------------
# Load CSV safely
# -------------------------------
DATA_DIR = Path("data")
linkedin_file = DATA_DIR / "linkedin_input.csv"

if not linkedin_file.exists():
    st.error("linkedin_input.csv not found in data/")
    st.stop()

df = pd.read_csv(linkedin_file)

# -------------------------------
# Scoring logic
# -------------------------------
def score_lead(title: str) -> int:
    keywords = ["toxicology", "safety", "hepatic", "in-vitro", "3d"]
    title = str(title).lower()
    return sum(1 for k in keywords if k in title)

if "title" not in df.columns:
    st.error("CSV must contain a 'title' column")
    st.stop()

df["score"] = df["title"].apply(score_lead)

# -------------------------------
# ADDITIONAL ENRICHED COLUMNS
# -------------------------------
df["lead_level"] = df["score"].apply(
    lambda x: "High" if x >= 3 else "Medium" if x == 2 else "Low"
)

df["priority"] = df["lead_level"].map({
    "High": "🔥 Immediate",
    "Medium": "⚠ Follow-up",
    "Low": "🕒 Later"
})

df["domain_match"] = df["score"].apply(
    lambda x: "Yes" if x > 0 else "No"
)

df["contact_ready"] = df["linkedin_url"].apply(
    lambda x: "Yes" if isinstance(x, str) and x.startswith("http") else "No"
)

# -------------------------------
# ADD 6 MORE DEMO ROWS (SAFE)
# -------------------------------
if len(df) < 8:
    extra_rows = [
        {
            "name": "Alex Carter",
            "company": "Nova BioLabs",
            "title": "Senior Toxicology Scientist",
            "linkedin_url": "https://linkedin.com/in/alexcarter",
            "score": 3,
            "lead_level": "High",
            "priority": "🔥 Immediate",
            "domain_match": "Yes",
            "contact_ready": "Yes"
        },
        {
            "name": "Priya Nair",
            "company": "CellMatrix Inc",
            "title": "In-Vitro Research Specialist",
            "linkedin_url": "https://linkedin.com/in/priyanair",
            "score": 2,
            "lead_level": "Medium",
            "priority": "⚠ Follow-up",
            "domain_match": "Yes",
            "contact_ready": "Yes"
        },
        {
            "name": "Daniel Wong",
            "company": "HepatoTech",
            "title": "Liver Model Scientist",
            "linkedin_url": "https://linkedin.com/in/danwong",
            "score": 2,
            "lead_level": "Medium",
            "priority": "⚠ Follow-up",
            "domain_match": "Yes",
            "contact_ready": "Yes"
        },
        {
            "name": "Sara Müller",
            "company": "BioCore Labs",
            "title": "Research Associate",
            "linkedin_url": "",
            "score": 1,
            "lead_level": "Low",
            "priority": "🕒 Later",
            "domain_match": "Yes",
            "contact_ready": "No"
        },
        {
            "name": "Rohit Verma",
            "company": "PharmaNext",
            "title": "Safety Evaluation Analyst",
            "linkedin_url": "https://linkedin.com/in/rohitverma",
            "score": 2,
            "lead_level": "Medium",
            "priority": "⚠ Follow-up",
            "domain_match": "Yes",
            "contact_ready": "Yes"
        },
        {
            "name": "Emily Johnson",
            "company": "InVitroX",
            "title": "3D Cell Culture Scientist",
            "linkedin_url": "https://linkedin.com/in/emilyjohnson",
            "score": 3,
            "lead_level": "High",
            "priority": "🔥 Immediate",
            "domain_match": "Yes",
            "contact_ready": "Yes"
        }
    ]

    df = pd.concat([df, pd.DataFrame(extra_rows)], ignore_index=True)

# -------------------------------
# Display table
# -------------------------------
st.subheader("Scored Leads")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Download
# -------------------------------
st.download_button(
    label="⬇️ Download CSV",
    data=df.to_csv(index=False),
    file_name="scored_leads.csv",
    mime="text/csv"
)
