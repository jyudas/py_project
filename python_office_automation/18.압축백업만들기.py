import os
import shutil

blacklist = ["Virus", "Malware", "Worm", "Trojan", "Ransomware", "Spyware"]
target_dir = "data"

for path, dirs, files in os.walk(target_dir):
    for dir in dirs:
        if dir.capitalize() in blacklist:
            dir_path = os.path.join(path, dir)
            shutil.rmtree(dir_path)


# 채점 코드
for contents in os.walk("data"):
    print(contents)