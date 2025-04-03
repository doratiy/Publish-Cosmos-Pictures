import telegram
from dotenv import load_dotenv
import os
import time
from fetch_nasa_pictures import get_nasa_pictures
from fetch_spacex_last_launch import get_spacex_urls
from fetch_epic_pictures import get_epic_pictures


def get_all_links(urls, token_nasa):
    epic_urls = []
    epic_urls = get_epic_pictures(epic_urls, token_nasa)
    links_spacex = get_spacex_urls()
    links_nasa = get_nasa_pictures(token_nasa)
    for link in links_spacex:
        urls.append(link)
    for link in links_nasa:
        urls.append(link)
    for link in epic_urls:
        urls.append(link)
    return urls


def tg_bot(urls, delay, chat_id):
    load_dotenv()
    token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(token=token)
    for link in urls:
        bot.send_photo(chat_id, link)
        time.sleep(delay)


if __name__ == "__main__":
    delay = 14400
    load_dotenv()
    token_nasa = os.environ["TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    epic_urls = []
    urls = []
    get_all_links(urls, token_nasa)
    tg_bot(urls, delay, chat_id)
