import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Chrome/94.0.4606.71'}

link = 'https://onedio.com/haber/kedi-ve-kopek-sahipleri-buraya-patili-dostlarimizla-ilgili-mutlaka-ogrenilmesi-gereken-13-onemli-bilgi-405688'

req = requests.get(link, headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')

title = soup.find_all('section', class_ = 'entry--image')

nameList = list()

for i in title:
    name= i.find('h2')
    nameList.append(name)
    print(name)
   
df = pd.DataFrame(data = nameList, columns=['title'])
df.to_csv('sample.csv', index=False, encoding = "utf-8")
    