# 추가할 문자열
str_1 = "업무 자동화는 실제 어떤 업무에 적용하고 사용할 지에 대해서 잘 아는게 중요하기 때문에\n"
str_2 = "개발 지식보다는 업무에 대한 이해가 높은 사람들이 오히려 더 잘 할 수 있습니다."

# 이곳에 코드를 작성해주세요.
with open("codeit.txt","a+",encoding="UTF-8") as file:
    file.write(str_1)
    file.write(str_2)
    file.seek(0)
    print(file.read())
