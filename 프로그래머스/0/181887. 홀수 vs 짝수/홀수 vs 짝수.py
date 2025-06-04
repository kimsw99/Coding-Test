def solution(num_list):
    a = 0
    b = 0
    for i, num in enumerate(num_list):
        if (i+1) % 2 == 0:
            a += num
        else:
            b += num
    if a > b:
        return a
    elif a < b :
        return b
    elif a == b :
        return b
        