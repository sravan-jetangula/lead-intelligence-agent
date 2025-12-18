import streamlit as st
from data_loader import load_data
from pubmed_agent import pubmed_score

def main():
    st.set_page_config(page_title="Lead Intelligence", layout="wide")

    st.title("Lead Intelligence Agent")

    if st.button("Run analysis"):
        with st.spinner("Running..."):
            df = load_data()
            st.dataframe(df.head())

if __name__ == "__main__":
    main()
