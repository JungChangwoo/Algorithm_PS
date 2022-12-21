# [전력망을 둘로 나누기]
# 전력망을 하나 끊어서 두 개의 네트워크 정점의 차이를 최소화하는 값을 구하시오
from collections import deque
def BFS(start, visited, graph):
    value = 0
    q = deque([start])
    while q:
        now = q.popleft()
        value += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return value


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    result = int(1e9)
    for a, b in wires:
        visited = [False] * (n + 1)
        visited[a] = True
        visited[b] = True
        lv = BFS(a, visited, graph)
        rv = BFS(b, visited, graph)
        result = min(result, abs(lv - rv))
    return result
