import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True) #워크북 모드
ws = wb.create_sheet('orangeBottle') #워크북생성
ws.append(['지점이름','주소','전화번호']) #행 추가

#response = requests.get("https://workey.codeit.kr/music")
#response = requests.get("https://workey.codeit.kr/ratings/index")

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 사용해서 HTML 코드 정리
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 지점에 대한 태그 가져오기
branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
    row = [
    # 각 태그에서 지점 이름, 전화번호 가져오기
    branch_tag.select_one('p.city').get_text(),
    branch_tag.select_one('p.address').get_text(),
    branch_tag.select_one('span.phoneNum').get_text()
    ]
    ws.append(row)

wb.save('오렌지_보틀.xlsx')