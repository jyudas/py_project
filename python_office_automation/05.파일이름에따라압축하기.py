# message = "..abcdeVBGGFCVh.."
# #변경
# print(message.replace("hh","zz"))
# #앞뒤 trim처리 문자 넣지 않을시 공백 default
# print(message.strip("."))
# print(message.lower())
# print(message.upper())

#
# import os
#
# filenames = ["git902.txt", "itc801.txt",
#              "ucl901.txt", "oop121.txt", "itp101.txt"]
#
# # 이곳에 코드를 작성해주세요.
# for file in filenames:
#     file_name, extension = file.split(".")
#     os.rename(file, file_name.upper() + "." + extension)
#
# # 채점 코드
# for file in os.listdir():
#     if file == "main.py":
#         continue
#     print(file)

# message = "동해물과백두산이마르고닳도록"
#
# print(message.find("백두산"))
# print(message.find("한라산"))
# print(message.count("백두산"))
#
# print("a" in "abcd")
#
# if "서해" in message :
#     print("T")
# else:
#     print("F")
#
# num = [1,3,5,6,9]
#
# print(3 in num)
# print(10 in num)

#  endwith() startwith()
# isalpha() : 문자
# isalnum() : 문자+숫자
# isdigit() : 숫자
#
# emails = ["choijw@codeit.com", "woojae@codeit.com",
#           "kyuri@github.com", "captain@codeit.kr", ]
#
# # 이곳에 코드를 작성해주세요.
# for i in emails:
#     if i.endswith("@codeit.com"):
#         print("{}으로 메일이 발송됩니다.".format(i))

import os
import zipfile

filenames = [
    "business_report.docsx", "codeit_account_book.pptx", "codeit_accounting_report.pptx",
    "codeit_cloud.png", "codeit_contract.hwp", "image_mac.svg",
    "KDW_report_01_2020-07-16.docx", "KHS_report_01_2020-07-16.docx", "money_book.xlsx",
]

zipfiles = []
# 이곳에 코드를 작성해주세요.
for i in filenames:
    if i.find("codeit") == 0:
        zipfiles.append(i)

with zipfile.ZipFile("codeit.zip", "w") as zip:
    for z in zipfiles:
        print(z)
        zip.write(z)

# 채점 코드
print(os.path.getsize("codeit.zip"))
