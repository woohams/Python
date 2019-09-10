# cmd - pip install beautifulsoup4
from bs4 import BeautifulSoup

import urllib.request

# urllib.request : 해당 url의 데이터를 가져온다.
# beautifulsoup : parsing

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)

#print(soup.findAll('dt', {'class', 'tit'}))

movieList = soup.findAll('dl', {'class', 'lst_dsc'})

for movieOne in movieList:
    link = movieOne.find('a')   # find는 가장 먼저 찾아주는 하나 !(첫 번째 a태그)
    num = movieOne.select('.num')[0] 
    print('{"name" : "%s", "star" : "%s"}' % (link.text, num.text))






    

