import os
filenames = ["news1.txt", "news2.txt", "news3.txt", "news4.txt", "news5.txt"]
codeit_news = []
codeit_counter = 0

# 이곳에 코드를 작성하세요.
for i in range(len(filenames)):
    with open(filenames[i], encoding="UTF-8") as file:
        if "코드잇" in file.read():
            codeit_news.append(filenames[i])
            file.seek(0)
            codeit_counter += file.read().count("코드잇")

# 채점 코드
print("코드잇이 포함된 뉴스 리스트: ")
print(codeit_news)
print("코드잇이 등장한 총 횟수: {}회".format(codeit_counter))

"""
스타트업 전문 기자로 일하고 있는 혜선이는 스타트업 관련 뉴스 중 "코드잇"이 들어간 뉴스만 정리해달라는 요청을 받았습니다. 
5개의 파일을 열어서 "코드잇" 이라는 글자가 있는 뉴스 파일을 codeit_news에 추가하고, 
모든 파일에서 "코드잇"이 등장한 총 횟수를 codeit_counter에 저장해 주세요.

-----------------
문자열 분리하고 합치기
split
split() 메서드를 쓰면, 특정 문자를 기준으로 문자열을 분리할 수 있으며 결과는 리스트 형태로 돌려줍니다. 이때 기준이 되는 문자를 "구분자"라고 합니다.
phone_number = "010-0000-1111"

text_list = phone_number.split("-")

print(text_list)  # ["010","0000","1111"]
print(type(text_list))  # <class 'list'>

# 전화번호 마지막 4자리만 필요하다면 이렇게 하면 되겠죠?
print(phone_number.split("-")[2])  # 1111
구분자를 아무것도 넣지 않으면 기본적으로는 공백이 구분자가 됩니다.
address = "서울특별시 종로구 세종로 청와대로 1"
print(address.split()) # ["서울특별시", "종로구", "세종로", "청와대로", "1"]
구분자를 '.'으로 하면 파일 이름과 확장자를 분리할 수 있습니다.
filename = "하품하는 고양이.jpeg"

name = filename.split(".")[0]
extension = filename.split(".")[1]

print("파일 이름: {}".format(name))
print("확장자: {}".format(extension))
참고로 파이썬에는 이런 문법도 가능합니다. 리스트로 된 두 값을 하나씩 넣어주는 거죠.
filename = "하품하는 고양이.jpeg"

name, extension = filename.split(".")

print("파일 이름: {}".format(name))
print("확장자: {}".format(extension))
splitext
파일 이름과 확장자를 분리할 때 아래와 같이 코드를 작성했습니다.
file = 'codeit_report.pdf'
filename, extension = file.split('.')
split() 메서드를 이용한 이 방법도 괜찮지만 확장자를 분리할 수 있는 다른 방법도 있습니다. 바로 os 모듈의 os.path.splitext() 함수를 사용하는 방법입니다. 기존의 split() 메서드를 사용하는 방법은 예외 상황이 많이 있습니다.  만약 파일 이름이 'codeit.report.txt'라면 어떻게 될까요? 이런 파일을 split() 메서드를 이용해 '.'을 기준으로 구분하게 되면 파일 이름과 확장자 두 개가 아니라 ['codeit', 'report', 'txt'] 이렇게 세 개의 원소를 가진 리스트가 됩니다.
file = 'codeit.report.pdf'
result = file.split('.') # ['codeit', 'report', 'pdf']
기존의 로직 대로면 여기서는 첫번째 원소가 'txt'가 아니라 'report'가 되고 이건 확장자가 아닙니다.
이 뒤에 확장자를 이용한 로직이 있다면 모두 잘못된 동작을 하거나 에러가 나게 되는거죠. 만약 파일 이름이 다양해지면 더 많은 경우의 수가 생기게 됩니다. 그래서 이런 모든 경우에도 예외 상황 없이 확장자를 분리해주는 함수가 바로 os.path.splitext()입니다.
import os

file = 'codeit.report.pdf'
filename, extension = os.path.splitext(file)
join
join() 메소드를 사용하면 반복 가능한 객체 안에 있는 문자열을 모두 합칠 수 있습니다. join() 메소드는 아래와 같은 구문을 갖고 있습니다. 반복 가능한 객체는 문자열, 리스트, 튜플형, 사전형등이 가능합니다. 우리는 문자열로 예를 들어 볼게요.
string.join(반복 가능한 객체)
아래와 같이 쓰면 어떤 결과가 나올까요?
str_1 = "codeit"
print(str_1.join("123"))
이런 결과가 나옵니다. 반복 가능한 객체를 하나로 합쳐주는데 그 사이사이에 str_1이 들어가 있는 형태인 거죠. 이 join() 메소드는 처음 사용하면 헷갈리는 경우가 많습니다. 다시 한번 천천히 읽어보시고 넘어가 주세요.
1codeit2codeit3
다음과 같은 핸드폰 번호 리스트가 있고, 이것을 하나의 문자열로 만드는데 '-'를 중간에 넣고 싶다면 이렇게 쓸 수 있는거죠.
phone_number_segments = ["010", "0000", "1111"]
print("-".join(phone_number_segments)) # 010-0000-1111
replace
replace() 메소드는 이름 그대로 문자열의 일부분을 다른 문자열로 바꿔주는 기능을 합니다. 바꾸고자 하는 문자열에서 호출하면 되는데, 이때 기존 문자열에서 바꾸고 싶은 부분과 바꿀 문자열을 순서대로 파라미터로 넣어주면 됩니다. 아래 코드를 실행하면 'Codeit'이라는 부분이 모두 '코드잇'으로 변경됩니다.
message = "Codeit은 여러분을 응원합니다. Codeit은 여러분과 함께합니다. 새로운 코딩 교육의 시작, Codeit!"

print(message.replace("Codeit", "코드잇")) 
# "코드잇은 여러분을 응원합니다. 코드잇은 여러분과 함께합니다. 새로운 코딩 교육의 시작, 코드잇!"
strip
strip() 메소드는 문자열의 처음과 끝에 있는 공백을 제거해주는 메소드입니다. 이때 제거되는 대상에는 공백(whitespace)도 있지만 이스케이프 문자 중 개행을 나타내는 '\n'이나 탭을 나타내는 '\t' 등도 포함됩니다. 보통 우리가 엔터를 입력해서 개행을 하게되면 눈에는 보이지 않지만 문자열 끝에 이스케이프 문자인 '\n'이 남는다고 설명했었죠? 그래서 일반적으로 문자열을 다룰때는 .strip()을 써서 의도치 않은 공백이나 개행을 제거해주는 것이 좋습니다. 그리고 strip 메소드는 문자열 중간에 있는 공백은 제거하지 않습니다.
message = " 새로운 코딩 교육의 시작, 코드잇 "

print(message)
print(message.strip()) # "새로운 코딩 교육의 시작, 코드잇"
만약 문자열 중간의 공백을 제거하고 싶다면 앞에서 설명한 replace메소드를 사용하면 됩니다.
message = "새로운 코딩 교육의 시작, 코드잇"
remove_whitespace = message.replace(" ", "")

print(remove_whitespace) # 새로운코딩교육의시작,코드잇
lower, upper , capitalize
이번에는 영어에 관련된 처리입니다. 메소드 이름이 모두 직관적이죠? lower()는 문자열을 모두 소문자로, upper()는 모두 대문자로, capitalize()는 앞 글자만 대문자로 하고 나머지는 모두 소문자로 바꾸는 메소드입니다. 파이썬은 대소문자를 구분하죠? 그러니까 'Apple'과 'apple'을 서로 다른 문자열로 취급합니다. 그래서 우리가 특정 영어 단어가 포함되어 있는지 여부를 확인할때는 보통 lower()나 upper()를 써서 문자열을 모두 소문자나 대문자로 바꿔놓고 찾는 것이 일반적입니다.
word = "codeIt"

print(word.lower()) # "codeit"
print(word.upper()) # "CODEIT"
print(word.capitalize()) # "Codeit"
find
주어진 문자열에서 내가 원하는 특정 문자열이 있는지를 체크하고 싶을때는 find() 메소드를 사용하면 됩니다. find() 메소드는 특정 문자열을 찾게되면 그 문자열이 시작하는 index를 결과로 돌려줍니다. 만약 찾는 문자열이 없으면 -1을 리턴합니다.
message = "코드잇 코딩 테스트 합격자: 최지웅, 오종훈, 성소원, 김대위"

print(message.find("오종훈")) # 21
print(message.find("최지웅")) # 16
print(message.find("유재석")) # -1
결과를 보면 "오종훈" 이라는 문자열은 21번째부터 나오고, "최지웅"은 16번째부터 나오고, "유재석"은 이 문자열에 없다는 걸 알 수 있네요.
count
count()는 메소드 이름대로 주어진 문자열에서 특정 문자열이 총 몇 번 나오는지 알려줍니다.
log = "카드 결제 기록: 코드잇 멤버십 구독, 쇼핑몰, 편의점, 쇼핑몰, 식당, 스트리밍 서비스 구독, 쇼핑몰, 핸드폰 요금"

print(log.count("쇼핑몰")) # 3
print(log.count("콘서트")) # 0
우리가 배운 걸 활용하면 이런 식으로 파일과 함께 활용할 수 도 있겠죠?
with open("william.txt") as file:
    content = file.read()
    print(content.count("윌리엄"))
in 연산자
문자열에 in 연산자를 쓰면, 특정 문자열이 주어진 문자열 안에 있는지 여부를 boolean값으로 리턴합니다.
print("A" in "ABCD") # True
print("ABC" in "ABCD") # True
print("E" in "ABCD") # False
in 연산자는 if문과 함께 많이 사용됩니다. 아래 코드는 log에서 쇼핑몰이라는 단어가 있는지 찾고 있다면 "쇼핑몰 기록이 발견되었습니다." 라고 출력하고, 없다면 "쇼핑몰 기록이 발견되지 않았습니다."를 출력합니다.
log = "카드 결제 기록: 코드잇 멤버십 구독, 쇼핑몰, 편의점, 쇼핑몰, 식당, 스트리밍 서비스 구독, 쇼핑몰, 핸드폰 요금"
keyword = "쇼핑몰"

if keyword in log:
    print("{} 기록이 발견되었습니다.".format(keyword))
else:
    print("{} 기록이 발견되지 않았습니다.".format(keyword))
# 쇼핑몰 기록이 발견되었습니다.
참고로, in 은 문자열뿐만 아니라 리스트, 튜플, 사전형등 반복 가능한 모든 객체에 사용할 수 있습니다.
numbers = [2, 3, 5, 7, 11]

print(3 in numbers)
print(10 in numbers)
endswith(), startswith()
endswith()는 문자열이 특정 단어로 끝나는지를, startswith()는 문자열이 특정 단어로 시작하는지에 대한 여부를 boolean형식으로 알려줍니다. 이 두 메소드를 활용하면 특정 이름을 가진 파일이나, 원하는 확장자를 가진 파일을 쉽게 찾을 수 있습니다.
filename1 = "file.txt"
filename2 = "photo.png"
str1 = "codeit_report"

print(filename1.endswith(".txt")) # True
print(filename1.endswith(".png")) # False
print(str1.endswith("repot") # True

print(filename2.startswith("photo")) # True
print(filename2.startswith("file")) # False
print(str1.startswith("codeit") # True
isalpha(), isalnum(), isdigit()
isalpha() 메소드는 어떤 문자열이 모두 문자로 이루어져 있으면  True를 아니라면 False를 리턴합니다. 메소드 이름에 'alpha'가 포함되어서 영어만 가능할 것 같지만 문자에는 영어와 한글이 모두 포함되어 문자열이 모두 영어나 한글로 이루어져 있다면 True를 리턴하고, 특수문자나 숫자, 공백이 문자열안에 포함되어 있으면 False를 리턴합니다.
text1 = "Codeit"
text2 = "코드잇"
text3 = "코드잇!"
text4 = "내가 좋아서 하는 코딩 공부 코드잇"
text5 = "코드잇123"

print(text1.isalpha())  # True
print(text2.isalpha())  # True
print(text3.isalpha())  # False
print(text4.isalpha())  # False
print(text5.isalpha())  # False
isalnum() 메소드는 alpha + number라고 생각하면 됩니다. 즉 isalpha() 메소드에서 숫자까지 포함된 문자열인지 여부를 체크해줍니다. 특수문자나, 공백이 문자열안에 포함되어 있으면 False를 리턴합니다.
text1 = "100ABC"
text2 = "혼자코딩공부하기좋은서비스1위코드잇"
text3 = "혼자 코딩 공부하기 좋은 서비스 1위 코드잇"
text4 = "5분이면 레슨 완료!"

print(text1.isalnum())  # True
print(text2.isalnum())  # True
print(text3.isalnum())  # False
print(text4.isalnum())  # False
만약 모두 숫자로 이루어져 있는지를 체크하고 싶다면 isdigit() 메소드를 사용하면 됩니다. 문자열이 모두 숫자로만 이루어져 있으면 True를 아니라면 False를 리턴합니다.
text1 = "0812"
text2 = "birthday0812"
text3 = "birthday"
text4 = "08 12"

print(text1.isdigit())  # True
print(text2.isdigit())  # False
print(text3.isdigit())  # False
print(text4.isdigit())  # False

"""