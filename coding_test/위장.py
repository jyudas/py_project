import collections
# 위장

def solution(clothes):
    d = collections.defaultdict(list)
    for k, v in clothes:
        d[v].append(k)

    closet = {}
    for cloth in d:
        # print(cloth)
        # print(len(d[cloth]))
        closet[cloth] = len(d[cloth])

    cal = 0
    for a in closet:
        b = closet[a]
        if cal == 0:
            cal = b + 1
        else:
            cal = cal * (b + 1)

    answer = cal - 1
    return answer

# 다른풀이
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer