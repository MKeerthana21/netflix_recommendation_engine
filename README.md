# 🎬Netflix_recommendation_engine
> ⚠️ This project is inspired by Netflix’s recommendation system. It is not affiliated with or endorsed by Netflix.

A personalized movie recommender system built using Python and Streamlit. It uses content-based filtering techniques and metadata from a movie dataset to suggest similar movies to users. This project also includes an exploratory data analysis (EDA) report.

---

## 🚀 Features

- 🔍 Search for a movie and get personalized recommendations
- 🎥 Recommendations based on genres, keywords, overview, and more
- 📊 EDA report analyzing movie data trends (PDF included)
- 🧠 Content-based recommendation using NLP techniques
- 💻 Simple and interactive Streamlit interface

##🧾 Project Structure

├── app.py # Streamlit frontend app

├── recommender.py # Core recommendation logic

├──netflix_titles.csv # Raw movie dataset

├── eda.pdf # Exploratory Data Analysis report

└── README.md # Project documentation

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
```
# Windows
```bash
venv\Scripts\activate
```
# macOS/Linux
```bash
source venv/bin/activate
```

3. Install Required Libraries
If your requirements.txt is too long, you can install the core libraries manually:

```bash
pip install streamlit pandas scikit-learn numpy
```
▶️ Run the App
```bash
streamlit run app.py
```
Go to http://localhost:8501 in your browser.
------------------------------------------------------------------------------------
 Exploratory Data Analysis
The eda.pdf contains a visual and statistical overview of the dataset, including:

Genre and popularity distribution

Yearly trends

Duration and language breakdowns
-----------------------------------------------------------------------------------------
 Recommendation Logic
The recommendation engine in recommender.py uses:

TF-IDF Vectorization on movie overviews

Cosine Similarity to find related movies

Top-N movie suggestion based on similarity score
-----------------------------------------------------------------------------------------
To Do:

 Improve recommendation algorithm with hybrid filtering

 Deploy the app using Streamlit Cloud or Render

 Add cleaned dataset version

 Add user feedback loop
