def solution(num_list):
    answer = []
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    answer = num_list
    return answer   

# 크지 않다 -> 작거나 같다