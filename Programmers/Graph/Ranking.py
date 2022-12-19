# [순위]
# 정확한 순위를 알 수 있는 갯수를 구하시오.
from collections import deque
def BFS(start, d, n, graph):
    count = 0
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for next in graph[now][d]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                count += 1
    return count

def solution(n, results):
    graph = [[[] for _ in range(2)] for _ in range(n+1)]
    for result in results:
        a, b = result
        graph[a][1].append(b)
        graph[b][0].append(a)
    result = 0
    for start in range(1, n+1):
        value = 0
        value += BFS(start, 0, n, graph)
        value += BFS(start, 1, n, graph)
        if value == n-1:
            result += 1
    return result