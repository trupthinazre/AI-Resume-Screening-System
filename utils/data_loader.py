import pandas as pd

def load_dataset(file_path):
    """
    Load the resume dataset.
    """
    df = pd.read_csv(file_path)
    return df