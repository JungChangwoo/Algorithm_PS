# [텀 프로젝트]
# 9466번
import sys
sys.setrecursionlimit(10**6)

def DFS(now):
  global result
  visited[now] = True
  cycle.append(now)

  next = graph[now]
  if visited[next]:
    if next in cycle:
      result -= len(cycle[cycle.index(next):])
    return
  else:
     DFS(next) 
  
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  n = int(sys.stdin.readline().rstrip())
  graph = [0] + list(map(int, sys.stdin.readline().split()))
  visited = [False] * (n+1)
  
  result = n
  for i in range(1, n+1):
    if not visited[i]:
      cycle = []
      DFS(i)
  print(result)
