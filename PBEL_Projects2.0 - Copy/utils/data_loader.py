import pandas as pd
from pathlib import Path


def load_courses():
    """Load courses.csv into a DataFrame."""
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "courses.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find courses file at: {csv_path}")

    return pd.read_csv(csv_path)
