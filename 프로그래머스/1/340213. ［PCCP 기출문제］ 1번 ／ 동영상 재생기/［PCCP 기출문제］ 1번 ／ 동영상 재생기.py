# 시간을 초단위로 변경하는 함수
def change_clock_sceond(clock):
    min, sec = clock.split(":")
    second_clcok = (int(min) * 60) + int(sec) 
    return second_clcok

# 시간을 "mm:ss"로 변경
def change_clock(result):
    min_str = (result // 60)
    if min_str < 10:
        min_str = "0"+ str(min_str)
    else:
        min_str = str(min_str)
    sec_str = (result % 60)
    if sec_str < 10:
        sec_str = "0"+ str(sec_str)
    else:
        sec_str = str(sec_str)
    
    return min_str+":"+sec_str
        
def solution(video_len, pos, op_start, op_end, commands):
    #1. 시간을 초단위로 변경
    op_start = change_clock_sceond(op_start)
    op_end = change_clock_sceond(op_end)
    video_len = change_clock_sceond(video_len)
    pos = change_clock_sceond(pos)
    
    if pos >= op_start and pos <= op_end:
            pos = op_end
            pass
            
    for command in commands:    
        if command == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        elif command == "next":
            if (video_len - pos) < 10:
                pos = video_len
            else:
                pos += 10 
                
        if pos >= op_start and pos <= op_end:
            pos = op_end
            pass
        
    return change_clock(pos)