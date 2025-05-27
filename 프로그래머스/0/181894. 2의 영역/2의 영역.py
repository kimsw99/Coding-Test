def solution(arr):
    two_list = []
    for i, num in enumerate(arr):
        if num == 2:
            two_list.append(i)
    
    if len(two_list) == 1:
        return [2]
    elif len(two_list) > 1:
        return arr[two_list[0]:two_list[-1]+1]
    return [-1]