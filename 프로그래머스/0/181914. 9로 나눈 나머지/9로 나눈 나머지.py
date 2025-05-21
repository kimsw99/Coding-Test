def solution(number):
    answer = 0
    for n in number:
        answer += int(n)
    answer %= 9
    return answer