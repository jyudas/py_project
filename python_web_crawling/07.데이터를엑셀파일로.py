import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True) #워크북 모드
ws = wb.create_sheet('TV Ratings') #워크북생성
ws.append(['순위','채널','프로그램','시청률']) #행 추가

#response = requests.get("https://workey.codeit.kr/music")

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),
        td_tags[2].get_text(),
        td_tags[3].get_text(),
    ]
    ws.append(row)

wb.save('시청률.xlsx') #행추가


"""
csv 버전
import csv
import requests
from bs4 import BeautifulSoup

# CSV 파일 생성
csv_file = open('시청률_2010년1월1주차.csv', 'w')
csv_writer = csv.writer(csv_file)

# 헤더 행 추가
csv_writer.writerow(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

"""
