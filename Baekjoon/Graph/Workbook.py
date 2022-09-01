# [문제집]
# 1766번
import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
in_count = [0] * (n+1)
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  in_count[b] += 1

def workbook():
  q = []
  for i in range(1, n+1):
    if in_count[i] == 0:
      heapq.heappush(q, i)
  while q:
    now = heapq.heappop(q)
    print(now, end=' ')
    for next in graph[now]:
      in_count[next] -= 1
      if in_count[next] == 0:
        heapq.heappush(q, next)

workbook()
