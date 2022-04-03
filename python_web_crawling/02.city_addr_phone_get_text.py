import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

div_tags = soup.select('div.branch')

branch_infos = []

for tag in div_tags:
    city_name = tag.select_one('p.city').get_text()
    address_name = tag.select_one('p.address').get_text()
    phone_number = tag.select_one('span.phoneNum').get_text()
    branch_infos.append([city_name,address_name,phone_number])

print(branch_infos)
