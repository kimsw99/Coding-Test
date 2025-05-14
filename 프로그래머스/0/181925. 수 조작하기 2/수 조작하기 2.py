# def solution(numLog):
#     answer = ''
#     for i in range(len(numLog))[1:]:
#         if  numLog[i] - numLog[i-1] == 1 :
#             answer += "w"
#         elif numLog[i] - numLog[i-1] == -1:
#             answer += "s"
#         elif numLog[i] - numLog[i-1] == 10:
#             answer += "d"
#         elif numLog[i] - numLog[i-1] == -10:
#             answer += "a"
#     return answer

def solution(numLog):
    control_map = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a'
    }
    
    return ''.join(control_map[numLog[i] - numLog[i - 1]] for i in 
                   range(1, len(numLog)))
