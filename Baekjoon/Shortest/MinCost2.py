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
    global gcount, gpath, minValue
    q = []
    heapq.heappush(q, [0, start, 1, [start]])
    d[start] = 0
    while q:
        dist, now, count, path = heapq.heappop(q)
        if now == end:
          if minValue > dist:
            gcount = count
            gpath = path
            minValue = dist
        if d[now] < dist:
            continue
        for next, value in graph[now]:
            cost = dist + value
            if cost < d[next]:
                d[next] = cost
                temp = path[:]
                temp.append(next)
                heapq.heappush(q, (cost, next, count+1, temp))
    
minValue = INF
gcount = 0
gpath = []
start, end = map(int, sys.stdin.readline().split())
dikstra(start, end)
print(d[end])
print(gcount)
print(*gpath)
