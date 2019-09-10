# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://sports.news.naver.com/wbaseball/record/index.nhn')
soup = BeautifulSoup(resp, 'html.parser')

sportsTeam = soup.findAll('div', {'class', 'inner'})

for sportsOne in sportsTeam:
    link = sportsOne.find('span')   
    menu = sportsOne.select('.name')
    print(link)




