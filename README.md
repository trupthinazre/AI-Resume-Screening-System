# 🤖 AI Resume Screening System

An AI-powered Resume Screening System that helps recruiters automatically evaluate and rank resumes based on a given Job Description. The application leverages Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity to identify the most relevant candidates through an interactive Streamlit dashboard.

---

## 🚀 Features

- 📄 Resume Screening using NLP
- 📋 Job Description Analysis
- 🧹 Resume Text Preprocessing
- 📊 TF-IDF Feature Engineering
- 📈 Cosine Similarity Matching
- ⭐ Recommendation Engine
- 📊 Recruiter Analytics Dashboard
- 🏆 Top Candidate Identification
- 📉 Resume Ranking
- 🎨 Interactive Streamlit UI
- 🌑 Modern Dark Theme Dashboard

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📂 Project Structure

```text
Resume-Screening-System
│
├── .streamlit
│   └── config.toml
│
├── app
│   ├── app.py
│   ├── styles.py
│   └── ui.py
│
├── assets
│
├── datasets
│   └── resume_dataset.csv
│
├── models
│
├── notebooks
│   └── Resume_Screening.ipynb
│
├── outputs
│   ├── resume_ranking.csv
│   └── Streamlit App - AI-Resume-Screening-System
│       ├── initial dashboard.png
│       ├── Result Generated (1).png
│       ├── Result Generated (2).png
│       └── Result Generated (3).png
│
├── utils
│   ├── data_loader.py
│   ├── recommendation.py
│   ├── screening_engine.py
│   ├── skill_comparison.py
│   ├── skill_extraction.py
│   ├── text_preprocessing.py
│   └── __init__.py
│
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/trupthinazre/AI-Resume-Screening-System.git
```

### Navigate to the Project Directory

```bash
cd AI-Resume-Screening-System
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app/app.py
```

---

## 📊 Workflow

1. Enter a Job Description.
2. Click **Analyze Resumes**.
3. The system preprocesses resumes and the job description using NLP.
4. TF-IDF converts textual data into numerical vectors.
5. Cosine Similarity calculates the similarity score between resumes and the job description.
6. Resumes are ranked according to their match score.
7. Recruiter Analytics and AI-based recommendations are displayed.

---

## 📸 Application Screenshots

### Initial Dashboard

![Dashboard](outputs/Streamlit%20App%20-%20AI-Resume-Screening-System/initial%20dashboard.png)

### Analysis Result

![Result 1](outputs/Streamlit%20App%20-%20AI-Resume-Screening-System/Result%20Generated%20(1).png)

### Recruiter Analytics

![Result 2](outputs/Streamlit%20App%20-%20AI-Resume-Screening-System/Result%20Generated%20(2).png)

### Resume Ranking

![Result 3](outputs/Streamlit%20App%20-%20AI-Resume-Screening-System/Result%20Generated%20(3).png)

---

## 📈 Future Enhancements

- Resume Upload (PDF/DOCX)
- Advanced Skill Extraction
- Skill Gap Analysis
- Interactive Plotly Visualizations
- PDF & CSV Report Export
- AI-based Resume Suggestions
- Multiple Job Description Comparison
- Deep Learning-Based Resume Matching

---

## Author

**Trupthi Nazre**

- GitHub: https://github.com/trupthinazre
- LinkedIn: https://www.linkedin.com/in/trupthi-nazre-k-289567327/
