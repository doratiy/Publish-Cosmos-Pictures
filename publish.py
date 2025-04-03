from tg_bot import tg_bot
from tg_bot import get_all_links
from dotenv import load_dotenv
import os
import random
import argparse


def publish(urls, delay, chat_id):
    random.shuffle(urls)
    tg_bot(urls, delay, chat_id)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description = 'Описание что делает программа'
    )
    parser.add_argument('-delay',
    '--delay',
    help = 'Ваша ссылка',
    default = 14400,
    type = int)
    args = parser.parse_args()
    delay = args.delay
    token_nasa = os.environ["TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    epic_urls = []
    urls = []
    get_all_links(urls, token_nasa)
    publish(urls, delay, chat_id)
