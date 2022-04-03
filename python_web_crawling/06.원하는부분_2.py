import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

popular_searches = []

print(soup.select_one('img'))
print(soup.select_one('img')['src'])
print(soup.select_one('img').attrs)