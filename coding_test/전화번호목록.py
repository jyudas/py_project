def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    # print(phoneBook)
    # print(list(zip(phoneBook, phoneBook[1:])))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


"""
다른풀이 
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    
    cnt=0
    for num in phoneBook:
        if len(phoneBook)-1 > cnt:
            org = len(phoneBook[cnt])
            str = phoneBook[cnt+1]
            
            if phoneBook[cnt] == str[0:org]:
                return False
        cnt += 1
    return True
"""