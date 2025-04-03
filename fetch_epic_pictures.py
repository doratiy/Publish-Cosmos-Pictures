import datetime
import requests
from dotenv import load_dotenv
import os


def get_epic_pictures(epic_urls, token):
    method_url = "https://api.nasa.gov/EPIC/api/natural/"
    date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    params = {
        "date": date,
        "api_key": token
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    num = 0
    for picture_num in range(5):
        picture = response.json()[picture_num]["image"]
        url_picture = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{picture}.png?api_key=suRmLdsmrorFtZKrJrqgpr8yD9zJWVtUkd2NmAOP"
        epic_urls.append(url_picture)
    return epic_urls


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["TOKEN"]
    epic_urls = []
    epic_urls = get_epic_pictures(epic_urls, token)
    print(epic_urls)
