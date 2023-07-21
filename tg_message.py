import os

import dotenv
from telegram import Bot

from neuro_format import neuro_format

dotenv.load_dotenv('.env')

bot = Bot(token=os.getenv('TG_TOKEN'))
chat_id = [279987360, 1286447667]


def send_message():
    final_post = neuro_format()
    if final_post is None:
        pass
    else:
        for id in chat_id:
            bot.send_message(id, final_post)
