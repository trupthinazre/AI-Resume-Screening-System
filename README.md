# 🤖 AI Resume Screening System

An AI-powered Resume Screening System that helps recruiters evaluate and rank resumes against a given Job Description using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 🚀 Live Demo

🔗 https://ai-resume-screening-system-nwyzmvvj2dnwftpvsqkdau.streamlit.app

---

## 📌 Features

- 📄 Resume Screening based on Job Description
- 🧠 NLP Text Preprocessing
- 📊 TF-IDF Vectorization
- 🎯 Cosine Similarity Matching
- ⭐ AI Recommendation Engine
- 📈 Recruiter Analytics Dashboard
- 📊 Resume Ranking Visualization
- 🌙 Modern Dark-Themed Streamlit UI
- ☁️ Deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- NLTK

### Machine Learning & NLP
- TF-IDF Vectorization
- Cosine Similarity
- Text Preprocessing
- Stopword Removal
- Lemmatization

### Deployment
- Streamlit Community Cloud

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Resume-Screening-System
│
├── app
│   ├── app.py
│   ├── styles.py
│   └── ui.py
│
├── datasets
│   └── resume_dataset.csv
│
├── notebooks
│   └── Resume_Screening.ipynb
│
├── outputs
│   ├── resume_ranking.csv
│   └── Streamlit App Screenshots
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
├── .streamlit
│   └── config.toml
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/trupthinazre/AI-Resume-Screening-System.git
```

Go to the project directory

```bash
cd AI-Resume-Screening-System
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## 📊 How It Works

1. Enter a Job Description.
2. The system preprocesses the text using NLP.
3. All resumes are converted into TF-IDF vectors.
4. Cosine Similarity is calculated between the Job Description and each resume.
5. Resumes are ranked based on similarity score.
6. Recommendations are generated based on match percentage.
7. The recruiter dashboard displays rankings, analytics, and visualizations.

---

## 📸 Screenshots

### Dashboard

- Modern Dark Theme UI
- Interactive Recruiter Dashboard
- Resume Ranking Table
- Match Score Analytics
- Recommendation Engine

Screenshots are available in the **outputs** folder.

---

## 🎯 Future Enhancements

- Resume PDF Upload
- Multiple Resume Upload
- Skill Gap Analysis
- Resume Parsing
- AI Interview Question Generation
- Download Results as Excel/PDF
- Candidate Skill Visualization
- LLM Integration (OpenAI/Gemini)

---

## Author

**Trupthi Nazre K**

- GitHub: https://github.com/trupthinazre
- LinkedIn: https://www.linkedin.com/in/trupthi-nazre-k-289567327/
