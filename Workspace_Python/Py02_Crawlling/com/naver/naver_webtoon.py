# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import json

resp = urllib.request.urlopen('https://comic.naver.com/webtoon/weekdayList.nhn?week=tue')
soup = BeautifulSoup(resp, 'html.parser')

webtoonList = soup.find('ul', {'class' : 'img_list'})
dl = webtoonList.select('dl')

res = {}
lst = list()

for chd in dl:
    title = chd.find('a').text
    star = chd.find('strong').text

    tmp = {}
    tmp['title'] = title
    tmp ['star'] = star
    lst.append(tmp)
    
res['webtoon'] = lst
res_json = json.dumps(res, ensure_ascii=False)

with open("webtoon.json", 'w', encoding='utf-8') as f:
    f.write(res_json)



