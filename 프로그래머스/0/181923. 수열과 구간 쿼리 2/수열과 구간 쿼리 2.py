def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        arr2 = []
        for i in arr[s:e+1]:
            if i > k :
                arr2.append(i)
        if len(arr2) > 0:
            answer.append(min(arr2))
        else:
            answer.append(-1)
    return answer