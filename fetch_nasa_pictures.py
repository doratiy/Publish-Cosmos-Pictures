import requests
from dotenv import load_dotenv
import os


def get_nasa_pictures(token):
    links_nasa = []
    method_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 30,
        "api_key": token
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    for response in (response.json()):
        if response["url"]:
            if response["media_type"] == "image":
                links_nasa.append(response["url"])
    return links_nasa


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["TOKEN"]
    links_nasa = get_nasa_pictures(token)
