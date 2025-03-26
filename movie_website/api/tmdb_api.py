import requests
from django.conf import settings

# Importing the api key and url
TMDB_API_KEY = settings.TMDB_API_KEY
TMDB_BASE_URL = "https://api.themoviedb.org/3"


# Function to get the popular movies
def get_popular_movies():
    url = f"{TMDB_BASE_URL}/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("results", [])

    # Print debug info if request fails
    print(f"Error: {response.status_code}, Response: {response.text}")
    return None
