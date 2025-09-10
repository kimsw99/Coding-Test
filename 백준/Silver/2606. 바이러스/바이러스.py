def dfs(graph, v, visited):
    visited[v] = True
    count = 1  # 현재 노드 포함
    
    for i in graph[v]:
        if not visited[i]:
            count += dfs(graph, i, visited)
    
    return count

com_count = int(input())   # 컴퓨터 수
list_count = int(input())  # 연결 수

graph = [[] for _ in range(com_count + 1)]

for _ in range(list_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)   # 양방향 그래프

visited = [False] * (com_count + 1)

# 1번 컴퓨터에서 시작
result = dfs(graph, 1, visited) - 1   # 자기 자신 제외

print(result)
