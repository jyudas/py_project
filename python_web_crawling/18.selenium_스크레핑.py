import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

popular = []

for artist in driver.find_elements_by_css_selector('ul.popular__order li'):
    popular.append(artist.text.strip())

print(popular)

