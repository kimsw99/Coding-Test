def solution(x1, x2, x3, x4):
    answer = True
    a1 = x1 or x2
    a2 = x3 or x4
    answer = a1 and a2
    return answer