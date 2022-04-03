import requests

### 코드를 작성하세요 ###
#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
rating_pages = []
for j in range (2010,2013): #2010 2011 2012
    for k in range (1,13): # 1~12
        for i in range (5): #0~4
            print("년:%s" ,j)
            print("월:%s" ,k)
            print("주차:%s", i)
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(j,k,i)
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)
# 출력 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드