# app.py

import streamlit as st
from recommender import recommend

st.set_page_config(page_title="Netflix Recommender", layout="centered")

st.title("🎬 Netflix Movie & Series Recommendation Engine")

movie = st.text_input("Enter a movie or series title:")

if movie:
    recommendations = recommend(movie)
    if recommendations[0] == 'Title not found. Try another.':
        st.error(recommendations[0])
    else:
        st.subheader("Top Recommendations:")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
