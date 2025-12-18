import streamlit as st
import app  # your existing app.py

st.set_page_config(page_title="Lead Intelligence Agent", layout="wide")

st.title("🔍 Lead Intelligence Agent")

st.info("App loaded successfully in Streamlit Cloud")

if st.button("Run Application"):
    st.write("Running core logic...")
    if hasattr(app, "main"):
        app.main()
    else:
        st.warning("No main() found in app.py")
