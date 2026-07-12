import utils
from utils.screening_engine import prepare_dataset

df = prepare_dataset("datasets/resume_dataset.csv")

print(df.head())

print("Utils imported successfully!")