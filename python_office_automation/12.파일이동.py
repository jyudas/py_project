count = 1
files = os.listdir("data")

for file in files:
    file_path = os.path.join("data", file)
    file_name, file_extension = os.path.splitext(file_path)

    if file_extension == ".png":
        new_file = "img_{}.png".format(count)
        count += 1
        new_file_path = os.path.join("img", new_file)
        os.rename(file_path, new_file_path)

# 채점 코드
print(os.path.getsize("img"))