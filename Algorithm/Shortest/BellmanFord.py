# [벨만 포드 알고리즘]
# 음수의 간선이 포함되어 있는 상황에서 최단거리 계산 가능
# 음의 사이클 존재 여부 확인 가능

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))
dist = [INF] * (n+1)

def bf(start):
  dist[start] = 0
  for i in range(n):
    for j in range(m):
      now, next, cost = edges[j]
      if dist[now] != INF and dist[next] > dist[now] + cost:
        dist[next] = dist[now] + cost
        if i == n-1:
          return True
  return False

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
dist = [INF] * (n+1)
def bf2(start):
  dist[start] = 0
  for i in range(n + 1):
    for j in range(n + 1):
      for next, cost in graph[j]:
        if dist[j] != INF and dist[next] > dist[j] + cost:
          dist[next] = dist[j] + cost
          if i == n-1:
            return True
  return False

negative_cycle = bf(1)
if negative_cycle:
  print("-1")
else:
  print("1")