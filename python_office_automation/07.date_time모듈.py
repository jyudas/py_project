import datetime

# birth_day=datetime.datetime(2022,2,25,16,14,00)
# print(birth_day)
# print(type(birth_day))

now = datetime.datetime.now()
print(now.strftime(("%Y/%m/%d")))
print(now.strftime("%H시 %M분 %S초"))

import datetime

datetime_1 = datetime.datetime(1989, 11, 22, 8, 3, 5)
datetime_2 = datetime.datetime(2002, 6, 29, 17, 11, 30)
datetime_3 = datetime.datetime(2020, 1, 26, 6, 14, 53)

# 이곳에 코드를 작성해주세요.
print(datetime_1.strftime("%Y/%m/%d"))
print(datetime_2.strftime("%I:%M:%S %p"))
print(datetime_3.strftime("%A %dth %B %Y"))
"""
datetime 모듈
파이썬에서 날짜와 시간 데이터를 다룰 때는 datetime 모듈을 많이 사용합니다. datetime 모듈을 사용하면 날짜와 시간을 datetime 객체로 만들어서 다루게 되는데, 이 datetime 객체 안에는 날짜와 시간 정보가 모두 들어있고 우리는 datetime 객체 자체로 날짜와 시간을 더하고 빼는 등의 연산을 할 수도 있고, 원하는 포맷으로 출력할 수도 있습니다.
datetime 객체 생성하기
먼저 특정 날짜에 대한 datetime 객체를 생성하려면 datetime.datetime() 함수를 사용하면 됩니다. 예를 들어 2020년 3월 14일을 datetime 객체로 생성하려면 아래와 같이 작성합니다. 시간 정보를 빼고 datetime 객체를 만들게 되면 시간 정보는 00시 00분 00초로 생성됩니다.
import datetime

birthday = datetime.datetime(2020, 3, 14)
print(birthday)
2020-03-14 00:00:00
만약 시간 정보도 넣고싶다면 파라미터로 함께 넣어주면 됩니다.
import datetime

birthday = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(birthday)

2020-03-14 13:06:15
현재 날짜와 시간 저장하기
바로 지금을 datetime 객체로 만들고 싶을 때는 datetime.datetime.now()를 사용합니다.
import datetime

now = datetime.datetime.now()
datetime 객체에서 날짜와 시간 가져오기
datetime 객체에서 날짜만 가져오고 싶을때는 date() 메소드를 사용하고 시간 정보를 가져오고 싶을때는 time() 메소드를 사용하면 됩니다.
import datetime

now = datetime.datetime.now()

print(now.date()) # 날짜만 추출 2021-06-23
print(now.time()) # 시간만 추출 19:16:07.623483
날짜와 시간 포맷에 맞춰서 출력하기
datetime 객체로부터 날짜와 시간을 가져올 때 기본 형식말고 원하는 대로 포맷을 바꿔주고 싶을때는 strftime() 메소드를 사용해서 원하는 포맷을 파라미터로 넣어주면 됩니다.
import datetime

datetime_object.strftime('my_format')
예를 들어, 2021-06-23 형식으로 표시하고 싶다면 포맷을 넣는 곳에 %Y/%m/%d 를 써주면 됩니다.
import datetime

now = datetime.datetime.now()
now_date = now.strftime('%Y/%m/%d')

print(now_date)  # 2021/06/23
그럼 시간도 한 번 해볼까요? 12시 11분 32초 형식으로 표시하고 싶다면, %H시 %M분 %S초 를 포맷으로 넘겨주시면 됩니다.
import datetime

now = datetime.datetime.now()
now_time = now.strftime('%H시 %M분 %S초')

print(now_time)  # 19시 41분 45초
물론 위 두 가지를 합칠 수도 있습니다.
import datetime

now = datetime.datetime.now()
now_format = now.strftime('%Y/%m/%d %H시 %M분 %S초')

print(now_format)  # 2021/06/23 19시 42분 49초
이밖에 표현하고 싶은 포맷이 있다면 아래 표에 있는 포맷 코드를 조합해서 사용하면 됩니다.
포맷코드	설명	예
%a	요일 줄임말	Sun, Mon, ... Sat
%A	요일	Sunday, Monday, ..., Saturday
%w	요일을 숫자로 표시, 월요일~일요일, 0~6	0, 1, ..., 6
%d	일	01, 02, ..., 31
%b	월 줄임말	Jan, Feb, ..., Dec
%B	월	January, February, …, December
%m	숫자 월	01, 02, ..., 12
%y	두 자릿수 연도	01, 02, ..., 99
%Y	네 자릿수 연도	0001, 0002, ..., 2017, 2018, 9999
%H	시간(24시간)	00, 01, ..., 23
%I	시간(12시간)	01, 02, ..., 12
%p	AM, PM	AM, PM
%M	분	00, 01, ..., 59
%S	초	00, 01, ..., 59
%Z	시간대	대한민국 표준시
%j	1월 1일부터 경과한 일수	001, 002, ..., 366
%U	1년중 주차, 월요일이 한 주의 시작으로	00, 01, ..., 53
%W	1년중 주차, 월요일이 한 주의 시작으로	00, 01, ..., 53
%c	날짜, 요일, 시간을 출력, 현재 시간대 기준	Sat May 19 11:14:27 2018
%x	날짜를 출력, 현재 시간대 기준	05/19/18
%X	시간을 출력, 현재 시간대 기준	'11:44:22'
datetime 모듈에 대해 더 궁금하다면 아래의 공식 문서를 참고해 주세요.
https://docs.python.org/ko/3/library/datetime.html
"""