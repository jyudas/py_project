from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')

driver.find_element_by_css_selector('.top-nav__login-link').click()
driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('.login-container__login-button').click()

driver.implicitly_wait(10)
#time.sleep(1)
"""
import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

popular_searches = []

rank_tags = soup.select('ul.rank__order li')


popular_artists = []
#popular__order class 안에 ul 태그 안에 li태그
for tag in rank_tags:
#    print(tag.get_text().strip())
    #print(list(tag.strings))
    #print(list(tag.stripped_strings)[1])
    popular_artists.append(list(tag.stripped_strings)[2])

print(popular_artists)
"""