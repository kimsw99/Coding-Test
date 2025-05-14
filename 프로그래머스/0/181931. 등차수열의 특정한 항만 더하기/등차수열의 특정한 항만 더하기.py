def solution(a, d, included):
    answer = 0
    for i,bool in enumerate(included):
        if bool and i==0:
            answer += a
            a+=d
        elif bool:
            answer +=a
            a+=d
        else:
            a+=d
    return answer