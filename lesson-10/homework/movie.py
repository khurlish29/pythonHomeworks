import requests
import random
def get_movie_recommendation(genre):
    api_key = "d0fc937e"
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']} (Rating: {movie['vote_average']})")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movie data.")

    