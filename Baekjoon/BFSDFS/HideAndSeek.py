# [숨바꼭질]
# 1697번
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
visited = [False] * 200001

def BFS():
  q = deque()
  q.append((n, 0))
  visited[n] = True
  while q:
    now, cost = q.popleft()
    if now == k:
      print(cost)
      break
    for next in (now+1, now-1, now*2):
      if 0 <= next < 200001:
        if not visited[next]:
          visited[next] = True
          q.append((next, cost + 1))
  
BFS()