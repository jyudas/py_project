import os
import shutil
import time

backup_time = time.strftime("%Y-%m-%d %H:%M:%s")
zip_file_name = "backup_{}".format(backup_time)
dst_path = os.path.join("backup", zip_file_name)

shutil.make_archive(dst_path, "zip", "data")
# 이곳에 코드를 작성해주세요.


#채점 코드
zip_file_path = os.path.join("backup", os.listdir("backup")[0])
print(os.path.getsize(zip_file_path))