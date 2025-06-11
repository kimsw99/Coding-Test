def solution(arr):
    answer = arr
    for i, num in enumerate(answer):
        if num >= 50 and num % 2 == 0:
            answer[i] = num / 2
        elif num < 50 and num % 2 == 1:
            answer[i] = num * 2
    return answer