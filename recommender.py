# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and clean data
df = pd.read_csv("netflix_titles.csv")
df = df.dropna(subset=['title'])

for col in ['director', 'cast', 'listed_in', 'description']:
    df[col] = df[col].fillna('')

df['content'] = df['title'] + ' ' + df['director'] + ' ' + df['cast'] + ' ' + df['listed_in'] + ' ' + df['description']

# Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['content'])

# Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index mapping
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

def recommend(title, cosine_sim=cosine_sim):
    title = title.lower()
    if title not in indices:
        return ['Title not found. Try another.']
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()
