import pandas as pd
from pathlib import Path

def load_data():
    data_dir = Path("data")
    df1 = pd.read_csv(data_dir / "funding_data.csv")
    df2 = pd.read_csv(data_dir / "linkedin_input.csv")
    return pd.concat([df1, df2], ignore_index=True)
