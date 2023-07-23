import requests
from bs4 import BeautifulSoup

from settings import PARSE_URL, SECTIONS

published_news = []


def parse_news():
    response = requests.get(PARSE_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    latest_news = soup.find_all('div', {'class': 'js-news-feed-item js-yandex-counter'})

    for one in range(5):
        news_link = latest_news[one].find('a', {'class': {'item__link'}})['href']
        item_bottom = latest_news[one].find('div', {'class': 'item__bottom'})
        news_data = item_bottom.find('a')
        try:
            news_photo = latest_news[one].find('img')['src']
        except:
            news_photo = None
        news_section = news_data.text.replace(',', '').replace('\xa0', '')

        try:
            if (
                news_link not in published_news
                and news_section in SECTIONS
                and news_photo is not None
            ):
                response = requests.get(news_link)
                response.encoding = 'utf-8'
                soup = BeautifulSoup(response.text, features='lxml')

                news_title = soup.find('h1').text
                content_block = soup.find(
                    'div', attrs={'class': 'l-col-center-590 article__content'}
                )
                text_block = content_block.find_all(['p', 'li'])
                text_block.encoding = 'utf-8'
                news_text = ''

                for tag in text_block:
                    if len(news_text) < 4097:
                        news_text += tag.news_text

                post = {
                    'section': news_section,
                    'title': news_title,
                    'text': news_text,
                    'picture': news_photo,
                    'link': news_link,
                }
                published_news.append(news_link)
                return post

            elif news_section not in SECTIONS:
                print(f'Неинтересно - {news_section}')
            elif news_photo is None:
                print('Есть новость без фото')
            elif news_link in published_news:
                print('Уже опубликована')
            else:
                print('Пока нет новостей')
        except:
            return None
