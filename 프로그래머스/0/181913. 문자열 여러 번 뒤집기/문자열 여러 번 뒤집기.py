def solution(my_string, queries):
    my_string = list(my_string)
    for s,e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)

#문자열(str)은 immutable(불변) 하기 때문에 직접 인덱스를 통해 값 변경을 할 수 없음.