import streamlit as st
import app  # your existing app.py

st.set_page_config(page_title="Lead Intelligence Agent", layout="wide")


    if hasattr(app, "main"):
        app.main()
    else:
        st.warning("No main() found in app.py")
