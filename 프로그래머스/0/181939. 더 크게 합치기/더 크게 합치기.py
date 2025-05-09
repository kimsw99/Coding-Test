def solution(a, b):
    answer = 0
    r1 = int(str(a) + str(b))
    r2 = int(str(b) + str(a))
    if r1 > r2:
        answer = r1
    elif r1 < r2 :
        answer = r2
    elif r1 == r2 :
        answer = r1
    return answer