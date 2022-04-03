import os
import shutil


# # 이곳에 코드를 작성해주세요.
# for i in range(1,31):
#     shutil.copy("diary.hwp", " diary_jan_{}.hwp".format(i))

# 채점 코드
for f in sorted(os.listdir()):
    print(f)
