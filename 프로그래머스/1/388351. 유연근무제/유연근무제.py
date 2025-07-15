def solution(schedules, timelogs, startday):
    pass_person = 0
    
    for i, timelog in enumerate(timelogs):
        is_pass = True  # 기본적으로 통과로 설정
        current_day = startday
        
        # 출근 희망 시각 + 10분 계산
        desired_time = schedules[i]
        hour = desired_time // 100
        minute = desired_time % 100
        
        # 10분 추가 후 시간 계산
        minute += 10
        if minute >= 60:
            hour += 1
            minute -= 60
        
        success_time = hour * 100 + minute
        
        # 7일간 출근 기록 확인
        for day_idx in range(7):
            # 토요일(6), 일요일(7)은 검사하지 않음
            if current_day not in [6, 7]:
                if timelogs[i][day_idx] > success_time:
                    is_pass = False
                    break
            
            # 다음 날로 이동
            current_day += 1
            if current_day > 7:
                current_day = 1
        
        if is_pass:
            pass_person += 1
    
    return pass_person