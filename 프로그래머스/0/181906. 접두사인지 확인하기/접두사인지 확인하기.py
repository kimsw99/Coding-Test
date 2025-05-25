def solution(my_string, is_prefix):
    answer = 0
    str_list = [my_string[:i] for i in range(len(my_string))]
    if is_prefix in str_list:
        return 1
    else:
        return 0