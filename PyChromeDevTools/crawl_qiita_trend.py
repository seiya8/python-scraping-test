import urllib.request
import time
import json

from bs4 import BeautifulSoup

url = 'https://qiita.com/'

time.sleep(1)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

article_list = []
for article in soup.select('article'):
    article_info = {}

    link = article.find('a', class_='style-15x5cbk')['href']
    title = article.find('a', class_='style-11rvgoz').text
    date = article.find('time').text
    tags = list(map(lambda x: x.text, article.find_all('a', class_='style-17yewao')))
    like = article.find('span', class_='style-17kunw6').text

    article_info['link'] = link
    article_info['title'] = title
    article_info['date'] = date
    article_info['tags'] = tags
    article_info['like'] = like

    article_list.append(article_info)

with open("qiita_article.json", "w") as f:
    json.dump(article_list, f, ensure_ascii=False)
