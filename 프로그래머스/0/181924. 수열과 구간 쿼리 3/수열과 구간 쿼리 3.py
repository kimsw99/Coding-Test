def solution(arr, queries):
    answer = []
    for i in queries:
        ch1_i = i[0]
        ch2_i = i[1]
        a = arr[ch1_i] 
        b = arr[ch2_i]
        arr[ch1_i] = b
        arr[ch2_i] = a
    answer = arr
    return answer