from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

def load_data():
    leads = pd.read_csv(DATA_DIR / "linkedin_input.csv")
    funding = pd.read_csv(DATA_DIR / "funding_data.csv")
    return leads.merge(funding, on="company", how="left")
