def solution(q, r, code):
    for i in range(len(code)):
        if i % q == r:
            code[i]
    return ''.join([code[i] for i in range(len(code)) if i % q == r])