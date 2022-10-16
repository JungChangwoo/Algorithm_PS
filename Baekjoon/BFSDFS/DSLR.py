# [DSLR]
# 9019번
import sys
from collections import deque
def DSLR(value, oper):
  if oper == 'D':
    return (value * 2) % 10000
  elif oper == 'S':
    if value == 0:
      return 9999
    value -= 1
    return value
  elif oper == 'L':
    value = ((value * 10) + (value // 1000)) % 10000
    return value
  else:
    value = ((value // 10) + ((value % 10) * 1000)) % 10000
    return value

dx = ['D', 'S', 'L', 'R']
def BFS(a, b):
  q = deque()
  q.append((a, ''))
  visited[a] = True
  while q:
    now, path = q.popleft()
    for d in range(4):
      next = DSLR(now, dx[d])
      if next == b:
        path += dx[d]
        print(path)
        return 
      if not visited[next]:
        visited[next] = True
        q.append((next, path + dx[d]))

for _ in range(int(sys.stdin.readline().rstrip())):
  a, b = map(int, sys.stdin.readline().split())
  INF = int(1e9)
  visited = [False] * 10001
  BFS(a, b)
  
