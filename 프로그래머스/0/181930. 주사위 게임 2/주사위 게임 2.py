def solution(a, b, c):
    answer = 0
    if a != b and b!=c and a!=c:
        answer += a + b + c
    elif a==b and b==c and a==c:
        answer += (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a==b and b!=c:
        answer += (a+b+c)*(a**2+b**2+c**2)
    elif b==c and b!=a:
        answer += (a+b+c)*(a**2+b**2+c**2)
    elif a==c and b!=a:
        answer += (a+b+c)*(a**2+b**2+c**2)
    return answer