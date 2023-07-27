import logging
from telegram import Bot

from app.neuro_format import neuro_format
from settings import CHAT_ID, TG_TOKEN, LOG_FORMAT, LOG_FILE

logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    filename=LOG_FILE,
    filemode='w',
)

bot = Bot(token=TG_TOKEN)


def create_message():
    """Функция формирует пост из преобразованных данных"""

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
    """Функция реализует отправку сообщения в telegram"""

    final_post, picture = create_message()
    if final_post is None:
        pass
    else:
        for id in CHAT_ID:
            try:
                bot.send_photo(id, picture, final_post, parse_mode='html')
            except Exception as error:
                logging.error(
                    f'Ошибка при отправке сообщения: {error}',
                    exc_info=True,
                )
                continue
    print(final_post)
