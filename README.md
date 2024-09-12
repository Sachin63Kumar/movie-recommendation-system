# CineChoice (Movie Recommendation System)

**CineChoice** is a movie recommendation system that helps users discover new movies based on their preferences. It uses advanced recommendation algorithms to suggest movies that are similar to the ones users like.

## Project Description

CineChoice provides an intuitive web interface where users can input their favorite movie and receive personalized recommendations. The system leverages movie similarity data and utilizes the TMDB API for fetching movie posters and additional information.

## Features

- **Movie Recommendations:** Get suggestions based on a selected movie's similarity.
- **Poster Display:** View movie posters for recommended films.
- **Responsive UI:** Access the recommendation system on various devices with a user-friendly interface.
- **Search Functionality:** Type and select movies from a dropdown for seamless recommendations.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Data Storage:** Pickle files for model and movie list
- **APIs:** TMDB API for movie details and posters

## Screenshots

Below are some screenshots of the CineChoice web interface:

![movie_recommendation](https://github.com/user-attachments/assets/077c2a59-b556-4b49-81f6-9594c8ce9383)
*Enter a movie name and get recommendations.*

![movie_recommendation2](https://github.com/user-attachments/assets/306458c5-b331-46d4-ab64-d099ec7546e9)
*Recommended movies with posters.*

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sachin63Kumar/movie-recommendation-system.git
    ```

2. Navigate into the project directory:
    ```bash
    cd movie-recommendation-system
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open your web browser and go to `http://localhost:running_port`.
2. Enter a movie name into the text field and click "Recommend" to receive movie recommendations.
3. View the recommended movies and their posters.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgments

- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) for movie data and posters.
- [Streamlit](https://streamlit.io/) for an easy-to-use frontend framework.
