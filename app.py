import streamlit as st
import pandas as pd
from pathlib import Path

from data_loader import load_data
from scorer import score_lead
from pubmed_agent import pubmed_score

st.set_page_config(
    page_title="3D In-Vitro Lead Intelligence Agent",
    layout="wide"
)

st.title("🧪 3D In-Vitro Lead Intelligence Agent")

DATA_DIR = Path("data")

@st.cache_data
def safe_load_data():
    try:
        return load_data()
    except Exception as e:
        st.error(f"Data loading failed: {e}")
        return None

def main():
    st.info("App started successfully on Streamlit Cloud ✅")

    df = safe_load_data()
    if df is None or df.empty:
        st.warning("No data available.")
        return

    st.subheader("📊 Input Leads")
    st.dataframe(df)

    if st.button("Run Lead Scoring"):
        with st.spinner("Scoring leads…"):
            scores = []
            for _, row in df.iterrows():
                try:
                    ps = pubmed_score(row.get("title", ""))
                    score = score_lead(row, ps)
                except Exception:
                    score = 0
                scores.append(score)

            df["score"] = scores

        st.success("Scoring completed ✅")
        st.subheader("🏆 Scored Leads")
        st.dataframe(df)

if __name__ == "__main__":
    main()
