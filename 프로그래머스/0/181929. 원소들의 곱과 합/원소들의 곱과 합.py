def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i 
        b += i
    b = b ** 2
    
    if a > b:
        return 0
    else:
        return 1