food_list = ["간고등어", "과메기", "굴비", "꽁치조림", "매운탕", "물회", "북엇국", "아귀찜", "오징어볶음"]

# 이곳에 코드를 작성하세요.
with open("food.txt",'w') as review_txt:
    review_txt.write("\n".join(food_list))

# 채점 코드
with open("food.txt", "r") as file:
    print(file.read())
