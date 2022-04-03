

# import requests
# from bs4 import BeautifulSoup
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
#
# driver.get("https://dhlottery.co.kr/gameResult.do?method=byWin")
# time.sleep(1)
#
# # data_base_1 = []
# data_base_2 = []
#
# init_ele = driver.find_elements_by_css_selector('.win_result')
# for init in init_ele:
#     init = init.find_element_by_css_selector('h4').text
#     init = init.replace("회 당첨결과","")
# # for i in range(1,int(init)+1):
# for i in range(1, 5):
#     lotto_base = []
#     CntCode_select = Select(driver.find_element_by_css_selector('#dwrNoList'))
#     CntCode_select.select_by_visible_text(str(i))
#     driver.find_element_by_css_selector('#searchBtn').send_keys(Keys.ENTER)
#     time.sleep(1)
#
#     ele_1 = driver.find_elements_by_css_selector('.win_result')
#     for j in ele_1:
#         yyyymmdd = j.find_element_by_css_selector('.desc').text
#         yyyymmdd = yyyymmdd.replace(" ","")
#         yyyymmdd = yyyymmdd.replace("년", ".")
#         yyyymmdd = yyyymmdd.replace("월", ".")
#         yyyymmdd = yyyymmdd.replace("일", "")
#         yyyymmdd = yyyymmdd.replace("추첨", "")
#         yyyymmdd = yyyymmdd.replace("(", "")
#         yyyymmdd = yyyymmdd.replace(")", "")
#
#         lotto_base.append(yyyymmdd[:4])
#         lotto_base.append(yyyymmdd[5:7])
#         lotto_base.append(yyyymmdd[8:10])
#
#     ele = driver.find_elements_by_css_selector('.nums')
#     for z in ele:
#         lottory = z.find_elements_by_css_selector('span.ball_645')
#         lotto_base.append("{}회 당첨결과".format(i))
#         for b in lottory:
#             lotto_base.append(b.text)
#
#     data_base_2.append(lotto_base)
#
# # print(data_base_1)
# print(data_base_2)
#
# for cnt in data_base_2:
#     for cc in cnt:
#         print(cc)
# ele = driver.find_elements_by_css_selector('.win_result')
# print(ele)
# for i in ele:
#     print( i.find_element_by_css_selector('.desc').text)
#     print( i.find_element_by_css_selector('h4').text)

# playlists = driver.find_elements_by_css_selector('.playlist__meta')

# for playlist in playlists:
#     title = playlist.find_element_by_css_selector('h3.title').text
#     hashtags = playlist.find_element_by_css_selector('p.tags').text
#     like_count = playlist.find_element_by_css_selector('span.data__like-count').text
#     music_count = playlist.find_element_by_css_selector('span.data__music-count').text
#     ws.append([title, hashtags, like_count, music_count])


    # url = API + param + str(i)
    #
    # response = requests.get(API)
    # rating_page = response.text
    #
    # soup = BeautifulSoup(rating_page, "html.parser")
    #
    # spans = soup.find_all('span', {'class': 'ball_645'})
    #
    # win_numbers = [span.get_text() for span in spans]
    #
    # print("round = ", i, "lines= ", win_numbers)

"""   
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 선거 웹사이트 접속
driver.get('http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03')
time.sleep(1)

# '국회의원선거'탭 클릭 
driver.find_element_by_css_selector('#electionId2').click()

# 서울특별시 선택
cityCode_select = Select(driver.find_element_by_css_selector('#cityCode'))
cityCode_select.select_by_visible_text('서울특별시')

# 종로구 선택
sggCityCode_select = Select(driver.find_element_by_css_selector('#sggCityCode'))
sggCityCode_select.select_by_visible_text('종로구') 

# '검색'버튼 클릭
driver.find_element_by_css_selector('#spanSubmit').click()
# 필요한 국회의원 정보 가져오기

# 웹 드라이버 종료
driver.quit()
"""
