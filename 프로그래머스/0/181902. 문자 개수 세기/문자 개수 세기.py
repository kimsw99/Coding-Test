# 아스키코드 대문자 알파벳 65 ~ 90, 소문자 97 ~ 122
def solution(my_string):
    return [my_string.count(chr(i)) for i in range(65,91)] + [my_string.count(chr(i)) for i in range(97, 123)]