# def solution(arr, idx):
#     answer = 0
#     bo = False 
    
#     for i, num in enumerate(arr):
#         if num == 1 and i >= idx:
#             answer = i 
#             bo = True
            
#     if bo == False:
#         return -1
    
#     return answer

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
