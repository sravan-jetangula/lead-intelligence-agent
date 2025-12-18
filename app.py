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
# Title
# -------------------------------
st.title("🔍 Lead Intelligence Agent")

# -------------------------------
# Run Application button (RELOCATED)
# -------------------------------
if st.button("▶ Run Application"):
    st.toast("Application running...", icon="🚀")

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
# ADDITIONAL SAFE COLUMNS
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
