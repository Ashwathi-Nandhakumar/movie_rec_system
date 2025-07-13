import streamlit as st
import pickle
import requests

# === Load data ===
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_titles = movies["title"].values

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Rec'D: Your Movie Wingman")

# === Initialize session state ===
if "titles" not in st.session_state:
    st.session_state.titles = []
if "posters" not in st.session_state:
    st.session_state.posters = []

selected_movie = st.selectbox("Pick a movie", movie_titles)

# === TMDB poster fetch ===
def get_poster_url(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNmVjZTYyZThhNThlYzYxODczZjcxYzU3MmQ3OTFlYSIsIm5iZiI6MTc1MTEwNjI5MC45NTksInN1YiI6IjY4NWZjMmYyYTUxYThmMjAxNDgwNWQzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9Aq65zGDvntHKk9NzpW4c8cW2s4MsBiQGUObZFsoF8s"
         }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"[Poster Fetch Error] ID={movie_id}, error={e}")
    return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

# === Recommendation Logic ===
def recommend(movie_title):
    index = movies[movies["title"] == movie_title].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

    recommended_titles = []
    recommended_posters = []

    for i in distances[1:6]:  # top 5
        movie_id = movies.iloc[i[0]].id
        title = movies.iloc[i[0]].title
        poster_url = get_poster_url(movie_id)
        recommended_titles.append(title)
        recommended_posters.append(poster_url)

    return recommended_titles, recommended_posters

# === Only fetch when button clicked ===
if st.button("Get Recommendations"):
    titles, posters = recommend(selected_movie)
    st.session_state.titles = titles
    st.session_state.posters = posters

# === Always render from session state ===
if st.session_state.titles and st.session_state.posters:
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(st.session_state.posters[i])
            st.text(st.session_state.titles[i])

 