# Intelligent Recommendation System for E-Learning Platforms

## What is this project?

This is a beginner Machine Learning project that recommends online courses based on a learner's interest.

It uses **content-based filtering**:
- Convert course text into numbers using **TF-IDF**
- Compare user interest with courses using **cosine similarity**
- Show the top matching courses in a web app

## Why this project?

E-learning platforms have many courses. A recommendation system helps learners find the most relevant courses faster, instead of searching manually.

## Features

- Simple web interface built with Streamlit
- Course dataset stored in CSV format
- Data loading helper using Pandas
- ML recommendations using Scikit-learn (TF-IDF + cosine similarity)
- Results shown with similarity scores

## Project structure

```text
PBEL_Projects2.0/
├── app.py                 # Main Streamlit web app (UI)
├── requirements.txt       # Python packages needed for this project
├── README.md              # Project documentation (this file)
├── data/
│   └── courses.csv        # Sample course dataset
├── models/                # Reserved for saved ML models later
└── utils/
    ├── data_loader.py     # Loads courses.csv into a Pandas DataFrame
    └── recommender.py     # ML recommendation logic
```

## Technologies used

- **Python** - main programming language
- **Streamlit** - web app interface
- **Pandas** - reading and handling course data
- **NumPy** - numerical support for ML
- **Scikit-learn** - TF-IDF vectorizer and cosine similarity

## How the recommendation works

1. User enters name and selects a learning interest.
2. App loads courses from `data/courses.csv`.
3. Each course's `category` + `tags` are converted into TF-IDF vectors.
4. User interest is also converted into a TF-IDF vector.
5. Cosine similarity score is calculated for every course.
6. Top 5 courses with the highest scores are displayed.

## How to run the project

### 1) Install required packages

```bash
pip install -r requirements.txt
```

### 2) Start the web app

```bash
streamlit run app.py
```

### 3) Open in browser

Streamlit will show a local URL (usually `http://localhost:8501`).  
Open it, enter your name, choose an interest, and click **Get Recommendations**.

## Sample viva explanation (30 seconds)

"This project is an intelligent course recommendation system for e-learning platforms. I built a Streamlit web app that takes a user's learning interest, loads course data from a CSV file, and recommends the most relevant courses using content-based filtering. The Machine Learning part uses TF-IDF to convert text into numbers and cosine similarity to rank the best matches."

## Future improvements

- Add user learning history for personalized recommendations
- Add collaborative filtering (users with similar behavior)
- Add difficulty-level filters (Beginner / Intermediate / Advanced)
- Save trained vectorizer/model files inside the `models/` folder
- Use a larger real-world course dataset
