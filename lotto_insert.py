import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pymysql

# db 정보
"""
연결옵션:

host - 서버주소. 자신의 컴퓨터를 서버로 사용한다면 ‘localhost’ 또는 127.0.0.1 을 입력.
user - username 입력
password - 서버 암호 입력
db - 데이터베이스, 스키마 이름 입력
charset - 문자세트 입력. 한글 사용을 위해 ‘utf8’ 입력
"""
conn = pymysql.connect(host='jyudas.synology.me', user='test', password='########', db='test', charset='utf8')
cur = conn.cursor()
sql = "insert into test_1 (yyyy, mm, dd, number_1, number_2, number_3, number_4, number_5, number_6, number_7) values (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"

driver = webdriver.Chrome()

driver.get("https://dhlottery.co.kr/gameResult.do?method=byWin")
time.sleep(1)

# data_base_1 = []
data_base_2 = []

init_ele = driver.find_elements_by_css_selector('.win_result')
for init in init_ele:
    init = init.find_element_by_css_selector('h4').text
    init = init.replace("회 당첨결과","")
for i in range(1,int(init)+1):
# for i in range(1, 5):
    lotto_base = []
    CntCode_select = Select(driver.find_element_by_css_selector('#dwrNoList'))
    CntCode_select.select_by_visible_text(str(i))
    driver.find_element_by_css_selector('#searchBtn').send_keys(Keys.ENTER)
    time.sleep(1)

    ele_1 = driver.find_elements_by_css_selector('.win_result')
    for j in ele_1:
        yyyymmdd = j.find_element_by_css_selector('.desc').text
        yyyymmdd = yyyymmdd.replace(" ","")
        yyyymmdd = yyyymmdd.replace("년", ".")
        yyyymmdd = yyyymmdd.replace("월", ".")
        yyyymmdd = yyyymmdd.replace("일", "")
        yyyymmdd = yyyymmdd.replace("추첨", "")
        yyyymmdd = yyyymmdd.replace("(", "")
        yyyymmdd = yyyymmdd.replace(")", "")

        lotto_base.append(yyyymmdd[:4])
        lotto_base.append(yyyymmdd[5:7])
        lotto_base.append(yyyymmdd[8:10])

    ele = driver.find_elements_by_css_selector('.nums')
    for z in ele:
        lottory = z.find_elements_by_css_selector('span.ball_645')
        lotto_base.append("{}회 당첨결과".format(i))
        for b in lottory:
            lotto_base.append(b.text)
    cnt = 0

    for k in lotto_base:
        print("cnt:{},k:{}".format(cnt,k))
        if cnt  == 0:
            lotto_0 = k
        elif cnt  == 1:
            lotto_1 = k
        elif cnt == 2:
            lotto_2 = k
        elif cnt == 4:
            lotto_4 = k
        elif cnt == 5:
            lotto_5 = k
        elif cnt == 6:
            lotto_6 = k
        elif cnt == 7:
            lotto_7 = k
        elif cnt == 8:
            lotto_8 = k
        elif cnt == 9:
            lotto_9 = k
        elif cnt == 10:
            lotto_10 = k
        cnt += 1

    cur.execute(sql, (lotto_0 ,lotto_1 ,lotto_2 ,lotto_4 ,lotto_5 ,lotto_6 ,lotto_7,lotto_8,lotto_9,lotto_10 ))

conn.commit()
cur.close()
