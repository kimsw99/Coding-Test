def solution(arr, query):
    a = arr
    for i, num in enumerate(query):
        if i % 2 == 0:
            a = a[:num+1]
        else:
            a = a[num:]
    return a