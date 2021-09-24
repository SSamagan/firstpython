import requests
from bs4 import BeautifulSoup as BS
import lxml
import json
link = "https://iro.oshsu.kg/pages/news_all/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
req = requests.get(url=link, headers=headers, verify=False)
soup = BS(req.text, "lxml")
cards = soup.find_all(class_ = 'box-box')
for el in cards:
    cards_title = el.find('header').text.strip()
    cards_url = el.find('a').get('href')
    cards_time = el.find('span').text.strip()
    print(cards_title, cards_url, cards_time)
    #YOOOOO