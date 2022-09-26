# [사회망 서비스(SNS)]
# 2533번
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
d = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(start):
  visited[start] = True
  d[start][0] = 1
  d[start][1] = 0

  for i in graph[start]:
    if not visited[i]:
      DFS(i)
      d[start][0] += min(d[i][0], d[i][1])
      d[start][1] += d[i][0]

DFS(1)
print(min(d[1][0], d[1][1]))




