import streamlit as st
import json
from tmdb_utils import get_movies_by_genres

# Load mood-genre mapping
with open("mood_genre_map.json") as f:
    mood_map = json.load(f)

# Emoji mapping for fun
mood_emoji = {
    "Happy": "😊",
    "Melancholy": "😢",
    "Stressed": "😤",
    "Energetic": "⚡",
    "In Love": "💕"
}

# Streamlit UI
st.set_page_config(page_title="StreamSparkle", page_icon="🎬")
st.title("🎬 StreamSparkle")
st.caption("Movie recommendations based on your mood ✨")

# Mood selector
mood = st.selectbox(
    "How are you feeling today?",
    options=list(mood_map.keys()),
    format_func=lambda m: f"{mood_emoji.get(m, '')} {m}"
)

if st.button("✨ Get Recommendations"):
    genre_ids = mood_map[mood]
    movies = get_movies_by_genres(genre_ids)

    if movies:
        for movie in movies:
            st.markdown("----")
            st.image(f"https://image.tmdb.org/t/p/w500{movie['poster_path']}")
            st.subheader(movie["title"])
            st.caption(movie["overview"])
    else:
        st.warning("No recommendations found. Try a different mood!")
