from telegram import Bot

from neuro_format import neuro_format
from settings import CHAT_ID, TG_TOKEN

bot = Bot(token=TG_TOKEN)


def create_message():
    post_data = neuro_format()
    if post_data is None:
        pass
    else:
        section = post_data['section']
        title = post_data['title']
        text = post_data['text']
        picture = post_data['picture']
        link = post_data['link']
        final_post = f'<b>{title}</b>\n\n{text}'
        return final_post, picture
    return None, None


def send_message():
    final_post, picture = create_message()
    for id in CHAT_ID:
        try:
            bot.send_photo(id, picture, final_post, parse_mode='html')
        except:
            continue
    print(final_post)
