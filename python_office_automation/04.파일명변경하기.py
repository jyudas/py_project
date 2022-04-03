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

message = "동해물과백두산이마르고닳도록"

print(message.find("백두산"))
print(message.find("한라산"))