# Intelligent Recommendation System for E-Learning Platforms

## 📌 What is this project?

This is a beginner Machine Learning project that recommends online courses based on a learner's interests.

It uses **content-based filtering**:
- Convert course text into numerical vectors using **TF-IDF**
- Compare user interests with courses using **Cosine Similarity**
- Recommend the most relevant courses through a simple web application

---

## 🎯 Why this project?

E-learning platforms contain thousands of courses, making it difficult for learners to find the most suitable ones. This recommendation system helps users quickly discover relevant courses based on their interests instead of manually searching through large catalogs.

---

## ✨ Features

- Beginner-friendly Machine Learning project
- Interactive web interface built with **Streamlit**
- Course dataset stored in CSV format
- Efficient data loading using **Pandas**
- Content-based recommendations using **TF-IDF** and **Cosine Similarity**
- Displays top recommended courses with similarity scores

---

## 📂 Project Structure

```text
PBEL_Projects2.0/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── data/
│   └── courses.csv        # Course dataset
├── models/                # Saved ML models (future use)
└── utils/
    ├── data_loader.py     # Loads dataset
    └── recommender.py     # Recommendation logic
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## ⚙️ How the Recommendation Works

1. The user enters their name and selects a learning interest.
2. The application loads the course dataset.
3. Course **category** and **tags** are combined and converted into TF-IDF vectors.
4. The user's selected interest is converted into a TF-IDF vector.
5. Cosine Similarity calculates how closely each course matches the user's interest.
6. The top five most relevant courses are displayed.

---

## 🚀 How to Run the Project

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Start the Streamlit application

```bash
streamlit run app.py
```

### 3. Open the application

Streamlit will generate a local URL (usually **http://localhost:8501**).

Open the URL in your browser, enter your name, select your learning interest, and click **Get Recommendations**.

---

## 💡 Project Explanation (Viva)

This project is an intelligent recommendation system for e-learning platforms. It uses **Content-Based Filtering** to recommend courses based on a learner's interests. The application converts course information into numerical vectors using **TF-IDF** and compares them with the user's interests using **Cosine Similarity**. The most relevant courses are then displayed through an interactive Streamlit interface.

---

## 🔮 Future Improvements

- Personalize recommendations using user learning history
- Implement Collaborative Filtering
- Add difficulty-level filters (Beginner, Intermediate, Advanced)
- Save trained models for faster predictions
- Integrate a larger real-world course dataset

---

## 👩‍💻 Author

Developed as a beginner Machine Learning project to understand recommendation systems, text vectorization, and similarity-based course suggestions.