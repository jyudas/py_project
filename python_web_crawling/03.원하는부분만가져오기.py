import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

print(soup.select('ul.popular__order'))

