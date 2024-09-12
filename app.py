import pickle
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")


# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()

    # Handle the case when 'poster_path' is not available
    if 'poster_path' in data:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    return None


# Recommendation function with improved ranking
def recommend(movie, num_recommendations):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations + 1]:
        movie_id = new.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        if poster:  # Ensure poster URL is valid
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(new.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


# Streamlit UI Design
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# Load data
new = pickle.load(open('gen_movie_list.pkl', 'rb'))  # Load the DataFrame as 'new'
similarity = pickle.load(open('gen_similarity.pkl', 'rb'))

# Dropdown for movie selection
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    new['title'].values  # Use 'new' to access movie titles
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
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, num_recommendations)

    # Determine number of columns for layout
    num_cols = min(num_recommendations, 5)  # Max 5 columns for better UI

    # Create layout with consistent image size
    cols = st.columns(num_cols)

    for i in range(num_recommendations):
        with cols[i % num_cols]:  # Distribute movies across columns
            st.image(recommended_movie_posters[i], use_column_width=True, width=200)
            st.markdown(f"<p style='text-align: center; font-weight: bold;'>{recommended_movie_names[i]}</p>",
                        unsafe_allow_html=True)
