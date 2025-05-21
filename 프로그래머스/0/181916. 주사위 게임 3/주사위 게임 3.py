from collections import Counter
#Counter 생성자에 문자열을 인자로 넘기면 각 문자가 문자열에서 몇 번씩 나타나는지를 알려주는 객체가 반환됩니다.

def solution(a, b, c, d):
    dice = [a,b,c,d]
    counter = Counter(dice)
    
    if len(counter) == 1:
        return 1111 * a
        
    if 3 in counter.values():
        for key, val in counter.items():
            if val == 3:
                p = key
            else:
                q = key
        return (10 * p + q)**2
    if len(counter) == 2:
        num = []
        for key, val in counter.items():
            num.append(key)
        return (num[0] + num[1]) * abs(num[0]-num[1]) 
    if len(counter) == 3:
        for key, val in counter.items():
            if val == 2:
                continue
            else:
               q1, q2 = [k for k, v in counter.items() if v == 1]
        return q1 * q2
    if len(counter) == 4:
        return min(dice)