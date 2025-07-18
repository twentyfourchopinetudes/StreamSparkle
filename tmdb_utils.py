import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def get_movies_by_genres(genre_ids, num_results=5):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": ",".join(genre_ids),
        "sort_by": "vote_average.desc",
        "vote_count.gte": 100
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["results"][:num_results]
