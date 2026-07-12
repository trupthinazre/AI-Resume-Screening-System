import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# -------------------------------------------------------
# Download NLTK resources (only if not already installed)
# -------------------------------------------------------

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# -------------------------------------------------------
# Initialize
# -------------------------------------------------------

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# -------------------------------------------------------
# Text Preprocessing Function
# -------------------------------------------------------

def preprocess_text(text):
    """
    Clean and preprocess resume/job description text.
    """

    # Handle missing values
    if text is None:
        return ""

    text = str(text)

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s()-]{8,}\d", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    words = text.split()

    # Remove stopwords and lemmatize
    cleaned_words = []

    for word in words:

        if word not in stop_words:

            cleaned_words.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(cleaned_words)