def solution(participant, completion):
    # 1. participant의 Counter를 구한다
    # 2. completion의 Counter를 구한다
    # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
    cnt = Counter()
    diff_persion = collections.Counter(participant) - collections.Counter(completion)

    # 4. counter의 key값을 반환한다
    answer = list(diff_persion.keys())[0]
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(answer)

    return answer

# 다른풀이
# import collections
#
#
# def solution(participant, completion):
#     # 1. participant 와 completion의 Counter를 구한다
#     dic_participant = collections.Counter(participant)
#     dic_completion = collections.Counter(completion)
#
#     # 2 key 값으로 for문 돌려 돌려
#     for key in collections.Counter(participant).keys():
#         # key 값이 completion에 있으면 완주한 선수
#         if dic_participant[key] != dic_completion[key]:
#             answer = key
#

#     return answer
# def solution(participant, completion):
#     answer = ''
#     for person in participant:
#         cnt = 0
#         for person2 in completion:
#             if(person == person2):
#                 continue
#             else :
#                 cnt = cnt+ 1
#             if (len(participant)-1 == cnt):
#                 answer = person
#     if(answer==''):
#         for person in participant:
#             person_cnt =participant.count(person)
#             person_cnt2 =completion.count(person)
#             if(person_cnt !=person_cnt2):
#                 answer = person
#     return answer