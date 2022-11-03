# [최소비용 구하기 2]
# 11779번
import sys
import heapq
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

INF = int(1e9)
d = [INF] * (n + 1)


def dikstra(start, end):
    q = []
    heapq.heappush(q, [0, start])
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for next, value in graph[now]:
            cost = dist + value
            if cost < d[next]:
                d[next] = cost
                heapq.heappush(q, (cost, next))
                path[next] = path[now][:]
                path[next].append(next)


start, end = map(int, sys.stdin.readline().split())
path = [[] for _ in range(n + 1)]
path[start].append(start)
dikstra(start, end)
print(d[end])
print(len(path[end]))
print(*path[end])
