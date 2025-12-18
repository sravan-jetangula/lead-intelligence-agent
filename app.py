import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------
# Page config (MUST be first)
# -------------------------------
st.set_page_config(
    page_title="3D In-Vitro Lead Intelligence Agent",
    layout="wide"
)



# -------------------------------
# Load CSV safely (NO external calls)
# -------------------------------
DATA_DIR = Path("data")

linkedin_file = DATA_DIR / "linkedin_input.csv"
funding_file = DATA_DIR / "funding_data.csv"

if not linkedin_file.exists():
    st.error(" linkedin_input.csv not found in data/")
    st.stop()

df = pd.read_csv(linkedin_file)



# -------------------------------
# Simple safe scoring (NO PubMed)
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
# Display
# -------------------------------
st.subheader("Scored Leads")
st.dataframe(df, use_container_width=True)

st.download_button(
    "⬇️ Download CSV",
    df.to_csv(index=False),
    "scored_leads.csv",
    "text/csv"
)


