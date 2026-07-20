import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_courses(courses_df, user_interest, top_n=5):
    """Recommend top_n courses using TF-IDF + cosine similarity."""
    df = courses_df.copy()
    df["content"] = df["category"].astype(str) + " " + df["tags"].astype(str)

    vectorizer = TfidfVectorizer(stop_words="english")
    course_matrix = vectorizer.fit_transform(df["content"])
    interest_vector = vectorizer.transform([user_interest])

    df["similarity"] = cosine_similarity(interest_vector, course_matrix).flatten()
    recommended = df.sort_values(by="similarity", ascending=False).head(top_n)
    return recommended.reset_index(drop=True)
