import requests


def get_spacex_urls():
    method_url = "https://api.spacexdata.com/v5/launches/"
    params = {
        "id": "5eb87d46ffd86e000604b388"
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    for response in reversed(response.json()):
        if response["links"]["flickr"]["original"]:
            return response["links"]["flickr"]["original"]


if __name__ == "__main__":
    links_spacex = get_spacex_urls()
