import os
from pathlib import Path

# file = open("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/aaa.txt")
# print(file.readline())
# print(file.readline())
# file.seek(0) #커서를 맨 앞으로 이동
# print(file.read())
# print(file.readlines())
# 인코딩처리
# file = open("text.txt", encoding="utf-8")
# for line in file:
#     print(line)
#
# file.close()
#with open 자동 close
# with open("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/aaa.txt") as file:
#     for line in file:
#         print(line)

# r 읽기 w쓰기  a :append
# with open("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/zzz.txt","w",encoding="UTF-8") as file:
#      pass

# os.rename("aaa.txt","bbb.txt")
# os.remove("aaa.txt","bbb.txt")

#경로 가져오기
# print(os.path.abspath("python_office_automation")+"/aaa.txt")
with open("hello.txt","a") as file:
    file.write("\nhello world")