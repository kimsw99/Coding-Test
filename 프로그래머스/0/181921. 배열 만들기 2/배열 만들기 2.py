def solution(l, r):
    from collections import deque
    result = []
    queue = deque(['5'])
    while queue:
        current = queue.popleft()
        num = int(current)
        if num > r:
            continue  
        if l <= num <= r:
            result.append(num)
        queue.append(current + '0')
        queue.append(current + '5')
    return sorted(result) if result else [-1]
