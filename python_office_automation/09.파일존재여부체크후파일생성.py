import os

for i in range(1, 51):
    filename = "client-{} report.txt".format(i)
    filepath = os.path.join("report", filename)

    if os.path.exists(filepath):
        print("{}번 고객님 설문지는 존재합니다.".format(i))
    else:
        print("{}번 고객님 설문지를 생성합니다.".format(i))

        with open(filepath, "w", encoding="utf-8") as newfile:
            newfile.write("{}번 고객님 설문지".format(i))