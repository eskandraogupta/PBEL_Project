import streamlit as st
from utils.data_loader import load_courses
from utils.recommender import recommend_courses

st.set_page_config(
    page_title="E-Learning Recommender",
    layout="wide"
)

st.title("Intelligent Recommendation System for E-Learning Platforms")
st.write(
    "Welcome! This app will recommend courses based on your interests and learning history."
)

courses_df = load_courses()

user_name = st.text_input("Enter your name:")
interest = st.selectbox(
    "What do you want to learn?",
    ["Python", "Machine Learning", "Web Development", "Data Science", "Other"]
)
level = st.selectbox(
    "Choose your preferred difficulty level:",
    ["All", "Beginner", "Intermediate", "Advanced"]
)

if st.button("Get Recommendations"):
    if user_name.strip() == "":
        st.warning("Please enter your name first.")
    else:
        st.success(f"Hello {user_name}! You selected: {interest} ({level})")

        if interest == "Other":
            st.info("Please choose a specific topic to see course recommendations.")
        else:
            filtered_courses = courses_df
            if level != "All":
                filtered_courses = courses_df[courses_df["level"] == level]

            if filtered_courses.empty:
                st.warning("Sorry, no courses found for this level.")
            else:
                recommended_df = recommend_courses(
                    courses_df=filtered_courses,
                    user_interest=interest,
                    top_n=5
                )

                if recommended_df.empty:
                    st.warning("Sorry, no recommendations found right now.")
                else:
                    recommended_df["similarity"] = recommended_df["similarity"].round(3)
                    st.write(
                        f"Top {len(recommended_df)} ML-based recommendation(s) for you:"
                    )

                    display_columns = [
                        "course_name",
                        "category",
                        "level",
                        "duration_hours",
                        "rating",
                        "similarity"
                    ]
                    st.dataframe(
                        recommended_df[display_columns],
                        use_container_width=True
                    )
                    st.caption(
                        "Recommendations use content-based filtering "
                        "(TF-IDF + cosine similarity), with an optional level filter."
                    )

st.caption("Built step by step as a beginner Machine Learning project.")
