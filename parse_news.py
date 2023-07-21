import requests
from bs4 import BeautifulSoup
import os
import dotenv

dotenv.load_dotenv('.env')

MAIN_URL = os.getenv('MAIN_URL')
published_news = []


def parse_news():
    response = requests.get(MAIN_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    breaking_news = soup.find('div', attrs={'data-vr-zone': 'Главная новость'})
    breaking_news_link = (breaking_news.find('a'))['data-vr-contentbox-url']

    latest_news = soup.find('div', {'data-vr-zone': 'Топ новости'})
    latest_news_link = (latest_news.find('a'))['data-vr-contentbox-url']

    if breaking_news_link not in published_news:
        response = requests.get(breaking_news_link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')

        title = soup.find('h1').text
        # description = soup.find('div', attrs={'class': 'article__text__overview'}).text
        content_block = soup.find(
            'div', attrs={'class': 'l-col-center-590 article__content'}
        )
        text_block = content_block.find_all(['p', 'li'])
        text_block.encoding = 'utf-8'
        news = ''

        for tag in text_block:
            if len(news) < 4097:
                news += tag.text

        post = {
            'title': title,
            # 'description': description,
            'news': news,
        }
        published_news.append(breaking_news_link)

        return post

    elif latest_news_link not in published_news:
        response = requests.get(latest_news_link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')

        title = soup.find('h1').text
        # description = soup.find('div', attrs={'class': 'article__text__overview'}).text
        content_block = soup.find(
            'div', attrs={'class': 'l-col-center-590 article__content'}
        )
        text_block = content_block.find_all(['p', 'li'])
        text_block.encoding = 'utf-8'
        news = ''

        for tag in text_block:
            if len(news) < 4097:
                news += tag.text

        post = {
            'title': title,
            # 'description': description,
            'news': news,
        }
        published_news.append(latest_news_link)

        return post

    else:
        print('Нока нет новостей')
