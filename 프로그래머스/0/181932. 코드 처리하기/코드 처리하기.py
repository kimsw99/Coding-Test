def solution(code):
    answer = ''  
    mode = 0
    for i, ch in enumerate(code):
        if ch == "1" and mode ==0:
            mode = 1
        elif ch == "1" and mode ==1:
            mode = 0
        elif mode ==0 and i%2 ==0:
            answer +=ch
        elif mode ==1 and i%2 ==1:
            answer +=ch
    if answer == "":
        answer = "EMPTY"
    return answer