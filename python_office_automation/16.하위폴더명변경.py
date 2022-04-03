import os

# 이곳에 코드를 작성해주세요.

target_path = "works"

for path, dirs, files in os.walk(target_path):
    for dir in dirs:
        if "코드잇" in dir:
            new_name = dir.replace("코드잇", "codeit")

            file_path = os.path.join(path, dir)
            new_path = os.path.join(path, new_name)
            os.rename(file_path, new_path)


# 채점 코드
for contents in os.walk('works'):
    print(contents)