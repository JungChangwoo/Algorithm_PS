# [웜홀]
# 1865번

def bf():
  for i in range(n):
    for j in range((m*2)+w):
      now, next, cost = edges[j]
      if dist[next] > dist[now] + cost:
        dist[next] = dist[now] + cost
        if i == n-1:
          return True
  return False

import sys
tc = int(sys.stdin.readline().rstrip())
INF = int(1e9)
for _ in range(tc):
  n, m, w = map(int, sys.stdin.readline().rstrip().split())
  edges = []
  for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b, c))
    edges.append((b, a, c))
  for _ in range(w):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b, -c))  
  dist = [INF] * (n+1)
  negative_cylcle = bf()
  if negative_cylcle:
    print('YES')  
  else:
    print('NO')