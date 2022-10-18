# [A -> B]
# 16953번
import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())

def get_next(now, d):
  if d == 0:
    return now * 2
  else:
    return (now * 10) + 1 

def BFS(a, b):
  q = deque()
  q.append((a, 0))
  while q:
    now, count = q.popleft()
    for d in range(2):
      next = get_next(now, d)
      if next == b:
        print(count + 2)
        return
      if 0 <= next <= b:
        q.append((next, count + 1))
  return False
if BFS(a, b) == False:
  print(-1)
        
    
