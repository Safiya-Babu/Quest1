import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def make_request(url, params):

    for i in range(3):
        try:
            response = requests.get(url, params=params, timeout=20)
            return response.json()

        except Exception:
            print("Retrying TMDB request...", i + 1)
            time.sleep(2)

    return {}

def search_tv_show(query: str) -> str:
    """Search for a Korean drama by drama name."""

    url = "https://api.themoviedb.org/3/search/tv"

    params = {
        "api_key": API_KEY,
        "query": query
    }

    data = make_request(url, params)

    if "results" not in data or len(data["results"]) == 0:
        return "No drama found."

    results = []

    for show in data["results"][:5]:
        name = show.get("name", "Unknown")
        overview = show.get("overview", "No overview available.")
        results.append(name + " - " + overview)

    return "\n".join(results)

def get_similar_shows(show_id: int) -> str:
    """Get Korean dramas similar to a TV show using its show id."""

    url = "https://api.themoviedb.org/3/tv/" + str(show_id) + "/similar"

    params = {
        "api_key": API_KEY
    }

    data = make_request(url, params)

    if "results" not in data or len(data["results"]) == 0:
        return "No similar dramas found."

    results = []

    for show in data["results"]:
        if "KR" in show.get("origin_country", []):
            results.append(show.get("name", "Unknown"))

        if len(results) == 5:
            break

    if len(results) == 0:
        return "No Korean similar dramas found."

    return "\n".join(results)

def discover_by_genre(genre_id: int) -> str:
    """Discover Korean dramas by genre id. Drama=18, Comedy=35, Mystery/Thriller=9648, Crime=80, Fantasy=10765, Action=10759."""

    url = "https://api.themoviedb.org/3/discover/tv"

    params = {
        "api_key": API_KEY,
        "with_genres": str(genre_id),
        "with_original_language": "ko",
        "sort_by": "popularity.desc",
        "first_air_date.gte": "2018-01-01"
    }

    data = make_request(url, params)

    if "results" not in data or len(data["results"]) == 0:
        return "No dramas found."

    results = []

    for show in data["results"][:5]:
        name = show.get("name", "Unknown")
        overview = show.get("overview", "No overview available.")
        results.append(name + " - " + overview)

    return "\n".join(results)

def search_person(actor_name: str) -> str:
    """Search for a Korean actor or actress by name and return their TMDB actor id."""

    url = "https://api.themoviedb.org/3/search/person"

    params = {
        "api_key": API_KEY,
        "query": actor_name
    }

    data = make_request(url, params)

    if "results" not in data or len(data["results"]) == 0:
        return "Actor not found."

    for person in data["results"]:
        known_for = person.get("known_for", [])

        for work in known_for:
            if "KR" in work.get("origin_country", []):
                return "Actor Name: " + person.get("name", "Unknown") + "\nActor ID: " + str(person.get("id"))

    person = data["results"][0]

    return "Actor Name: " + person.get("name", "Unknown") + "\nActor ID: " + str(person.get("id"))


def get_person_tv_credits(person_id: int) -> str:
    """Get Korean dramas acted by a person using their TMDB actor/person id."""

    url = "https://api.themoviedb.org/3/person/" + str(person_id) + "/tv_credits"

    params = {
        "api_key": API_KEY
    }

    data = make_request(url, params)

    if "cast" not in data or len(data["cast"]) == 0:
        return "No TV credits found."

    results = []

    for show in data["cast"]:
        name = show.get("name", "Unknown")
        country = show.get("origin_country", [])
        character = show.get("character", "")

        if "KR" in country:
            if character:
                results.append(name + " as " + character)
            else:
                results.append(name)

        if len(results) == 5:
            break

    if len(results) == 0:
        return "No Korean dramas found for this actor."

    return "\n".join(results)