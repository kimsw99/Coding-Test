def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer)

#사전순서 정렬 sorted