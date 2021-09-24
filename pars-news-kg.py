import requests
from bs4 import BeautifulSoup as BS
import lxml
import json
link = "https://iro.oshsu.kg/pages/news_all/"
headers={
    "Hello "
}
req = requests.get(url=link, headers=headers, verify=False)
soup = BS(req.content, "lxml")
title = soup.find_all('a', class_ = 'image-post')
for el in title:

    print(el.text)