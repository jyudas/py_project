import os

target_dir = "data"
files = os.listdir(target_dir)
total_size = 0

for file in files:
    file_path = os.path.join(target_dir, file)
    file_size = os.path.getsize(file_path)

    print("{}의 용량은 {}byte입니다.".format(file, file_size))
    total_size += file_size

print("총 용량은 {}byte입니다.".format(total_size))