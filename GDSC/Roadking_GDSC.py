from collections import deque
def BFS(edge1, edge2, graph, n):
    visited = [False] * n
    left_count = 0
    right_count = 0
    q = deque()
    q.append((edge1, 'left'))
    q.append((edge2, 'right'))
    visited[edge1] = True
    visited[edge2] = True
    while q:
        now, d = q.popleft()
        if d == 'left':
            left_count += 1
        else:
            right_count += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next, d))
    total = left_count * right_count * 2
    return total

def solution(edges):
    n = len(edges) + 1
    result = 0
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        edges[i] = list(map(int, edges[i]))
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    for edge in edges:
        value = BFS(edge[0], edge[1], graph, n)
        result = max(result, value)
    return result