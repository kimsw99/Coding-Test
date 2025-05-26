def solution(my_string, indices):
    answer = ''
    for i,str  in enumerate(my_string):
        if not i in indices:
            answer += str
    return answer