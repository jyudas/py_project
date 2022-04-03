# reviews = ["computer_science.txt", "git.txt",
#            "python_programming.txt", "web_publishing.txt"]
#
# # 이곳에 코드를 작성해주세요.
#
#
# # 채점 코드
# with open("all_reviews.txt") as review_txt:
#     print(review_txt.read().strip())

reviews = ["computer_science.txt", "git.txt",
           "python_programming.txt", "web_publishing.txt"]

# 이곳에 코드를 작성해주세요.
for i in reviews:
    f_name = open(i)
    with open("all_reviews.txt", "a", encoding="UTF-8") as file:
        for line in f_name:
            file.write(line)
        file.write("\n\n")

# 채점 코드
with open("all_reviews.txt") as review_txt:
    print(review_txt.read().strip())
