import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.data_loader import load_dataset
from utils.text_preprocessing import preprocess_text
from utils.recommendation import get_recommendation


def screen_resumes(job_description, dataset_path):
    """
    Screen resumes against the given Job Description.
    """

    # Load dataset
    df = load_dataset(dataset_path)

    # Preprocess resumes
    df["Cleaned_Resume"] = df["Resume"].apply(preprocess_text)

    # Preprocess JD
    cleaned_jd = preprocess_text(job_description)

    # TF-IDF
    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(
        df["Cleaned_Resume"].tolist() + [cleaned_jd]
    )

    # Resume vectors
    resume_vectors = tfidf_matrix[:-1]

    # JD vector
    jd_vector = tfidf_matrix[-1]

    # Similarity
    similarity_scores = cosine_similarity(
        resume_vectors,
        jd_vector
    ).flatten()

    # Convert to percentage
    df["Match Score"] = similarity_scores * 100

    # Recommendation
    df["Recommendation"] = df["Match Score"].apply(get_recommendation)

    # Sort
    df = df.sort_values(
        by="Match Score",
        ascending=False
    )

    return df