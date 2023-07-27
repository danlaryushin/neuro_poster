from settings import CHAT_ID, TG_TOKEN
from telegram import Bot

from app.neuro_format import neuro_format

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
        final_post = f'<b>{title}</b>\n\n{text}\n'
        return final_post, picture
    return None, None


def send_message():
    final_post, picture = create_message()
    for id in CHAT_ID:
        try:
            bot.send_photo(id, picture, final_post, parse_mode='html')
            print(id)
        except:
            print('Не удалось отправить сообщение')
            continue
    print(final_post)
