def solution(my_string, m, c):
    answer = ''
    str_list = []
    count = len(my_string)//m 
    if len(my_string) % m > 0:
        count += 1 
    for i in range(count):
        str_list.append(my_string[m*i: m*(i+1)])
    return ''.join(str_list[i][c-1] for i in range(len(str_list)))