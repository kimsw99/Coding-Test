def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] = arr[i] + 1
    answer = arr
    return answer