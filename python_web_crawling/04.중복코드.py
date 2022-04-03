import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

#print(soup.select('ul.popular__order'))

popular_artists = []
#popular__order class 안에 ul 태그 안에 li태그
for tag in soup.select('ul.popular__order li'):
#    print(tag.get_text().strip())
    #print(list(tag.strings))
    #print(list(tag.stripped_strings)[1])
    popular_artists.append(list(tag.stripped_strings)[1])

print(popular_artists)
