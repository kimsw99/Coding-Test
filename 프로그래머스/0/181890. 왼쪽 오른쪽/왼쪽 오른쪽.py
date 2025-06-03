def solution(str_list):
    for i, str in enumerate(str_list):
        if str == "l":
            return str_list[:i]
        elif str == "r":
            return str_list[i+1 :]
    return []
