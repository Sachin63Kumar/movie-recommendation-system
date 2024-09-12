import streamlit as st
import pandas as pd
import numpy as np
import pickle
import gdown
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# Google Drive file IDs
SIMILARITY_FILE_ID = '1gkzSrV47t8A7xmXs5xwkn3iG9heomhw2'
MOVIE_LIST_FILE_ID = '1iSziCsnmLrB9BiwwWmRrt5Z7rmzKsm7y'


# Function to download files from Google Drive using gdown
def download_file_from_google_drive(file_id, destination):
    URL = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(URL, destination, quiet=False)


# Check if files exist; if not, download them
if not os.path.exists('gen_similarity.pkl'):
    download_file_from_google_drive(SIMILARITY_FILE_ID, 'gen_similarity.pkl')

if not os.path.exists('gen_movie_list.pkl'):
    download_file_from_google_drive(MOVIE_LIST_FILE_ID, 'gen_movie_list.pkl')


# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    if 'poster_path' in data:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    return None


# Load the pre-trained model and movie list
with open('gen_similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

with open('gen_movie_list.pkl', 'rb') as f:
    movie_list = pickle.load(f)


# Recommendation function with improved ranking
def recommend_movies(movie_name, num_recommendations):
    if movie_name not in movie_list['title'].values:
        st.error("Movie not found in the database.")
        return [], []

    index = movie_list[movie_list['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:num_recommendations + 1]:
        movie_id = movie_list.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        if poster:
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(movie_list.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit UI Design
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# Dropdown for movie selection
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list['title'].values  # Use 'movie_list' to access movie titles
)

# Input field for number of recommendations
num_recommendations = st.number_input(
    "Number of Recommendations",
    min_value=1,
    max_value=20,
    value=5
)

# When 'Show Recommendation' button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend_movies(selected_movie, num_recommendations)

    if not recommended_movie_names:
        st.write("No recommendations available.")
    else:
        # Determine number of columns for layout
        num_cols = min(num_recommendations, 5)  # Max 5 columns for better UI

        # Create layout with consistent image size
        cols = st.columns(num_cols)

        for i in range(num_recommendations):
            with cols[i % num_cols]:  # Distribute movies across columns
                st.image(recommended_movie_posters[i], use_column_width=True, width=200)
                st.markdown(f"<p style='text-align: center; font-weight: bold;'>{recommended_movie_names[i]}</p>",
                            unsafe_allow_html=True)
