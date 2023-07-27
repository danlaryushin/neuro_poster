import openai
from settings import API_KEY

from app.parse_news import parse_news

openai.api_key = API_KEY


def neuro_format():
    news_data = parse_news()
    if news_data is None:
        return None

    title = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'Создай короткий заголовок на русском языке из такста:',
            },
            {'role': 'user', 'content': news_data['title']},
        ],
    )

    text = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'Ты - новостной обозреватель. Сократи текст до 2 предложений, сохранив смысл. Ответь на русском языке ',
            },
            {'role': 'user', 'content': news_data['text']},
        ],
    )

    news_section = news_data['section'].upper()
    news_title = title.choices[0].message.content
    news_title.encode('utf-8')
    news_text = text.choices[0].message.content
    news_text.encode('utf-8')
    news_picture = news_data['picture']
    news_link = news_data['link']

    post = {
        'section': news_section,
        'title': news_title,
        'text': news_text,
        'picture': news_picture,
        'link': news_link,
    }

    return post
