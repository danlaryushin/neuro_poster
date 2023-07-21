import os

import dotenv
import openai

from parse_news import parse_news

dotenv.load_dotenv('.env')

openai.api_key = os.getenv('API_KEY')


def neuro_format():
    news_data = parse_news()
    if news_data is None:
        return None

    title = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'Скажи другими словами'},
            {'role': 'user', 'content': news_data['title']},
        ],
    )

    """description = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Скажи другими словами"},
            {"role": "user", "content": news_data["description"]},
        ],
    )"""

    text = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'Перескажи в два предложения',  # 'Резюмируй текст'
            },
            {'role': 'user', 'content': news_data['news']},
        ],
    )

    news_title = title.choices[0].message.content
    news_title.encode('utf-8')
    # news_description = description.choices[0].message.content
    news_text = text.choices[0].message.content
    news_text.encode('utf-8')
    final_post = news_title + '\n\n' + news_text

    print(final_post)
    return final_post
