from collections import deque

def move_point(n, k):

    MAX = 100001
    visited = [False]*MAX
    queue = deque()
    queue.append((n, 0))
    visited[n] = True

    while queue:
        n, cnt = queue.popleft()

        if n == k:
            break
        
        # 현재 위치에서 3가지 방향으로 확인
        for i in (n-1, n+1, n*2):
             if 0 <= i < MAX and not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return cnt

n, k= map(int, input().split())

# BFS를 수행한 결과 출력
print(move_point(n, k))