import shutil
import os

# 1. 복구용 모든 압축 파일을 출력
count = 0
zip_files = os.listdir("backup")
for zip_file in zip_files:
    print("{}번 파일: {}".format(count, zip_file))  # 출력 포맷
    count += 1

# 2. 복구용 압축 파일 선택
backup_num = 1  # 원하는 백업 번호 지정

backup_zip = zip_files[backup_num]  # 백업 파일 선택
backup_zip_path = os.path.join("backup", backup_zip)



# 3. 기존 폴더 삭제
shutil.rmtree("data")

# 4. zip 파일을 이용해서 파일 복구
print("{}번 파일: {} 버전으로 복구됩니다.".format(backup_num, backup_zip))
shutil.unpack_archive(backup_zip_path, "data")

# 채점 코드
print("\ndata dirs")
for contents in os.walk("data"):
    print(contents)