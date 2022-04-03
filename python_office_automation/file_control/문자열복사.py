# 이곳에 코드를 작성해주세요.
with open("log.txt") as log_file:
    log = log_file.read()


with open("error_log_jan.txt",'w') as file:
    file.write("january error log\n")
    file.write(log)

# 채점 코드
import os
print(os.path.getsize("error_log_jan.txt"))