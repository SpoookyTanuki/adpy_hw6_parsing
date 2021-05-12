import requests
from bs4 import BeautifulSoup, Tag

KEYWORDS = {'Научно-популярное', 'Программирование', 'Python'}

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('response is not valid')

soup = BeautifulSoup(response.text, features="html.parser")
for article in soup.find_all('article'):
    hubs = {h.text for h in article.find_all('a', class_='hub-link')}

    all_texts = {k.text for k in soup.find_all('div', class_='post__text_v2')}

    for one_text in all_texts:
        split_words = set(one_text.split())

        if split_words & KEYWORDS:
            title: Tag = article.find('h2', class_='post__title')
            a: Tag = title.find('a')
            href = a.attrs.get('href')
            data: Tag = article.find('span', class_='post__time')
            print(f'{data.text}{title.text}{href}\n')