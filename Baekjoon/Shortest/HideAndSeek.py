# [숨바꼭질 3]
# 13549번
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
distance = [INF] * 1000001

from collections import deque
def HideAndSeek(start, end):
  q = deque([(0, start)])
  distance[start] = 0
  while q:
    dist, now = q.popleft()
    if now == end:
      return dist
    if now <= 0 or now >= 100000:
      continue
    if dist > distance[now]:
      continue
    # -1 
    next = now - 1
    cost = dist + 1
    if cost < distance[next]:
      distance[next] = cost
      q.append((cost, next))
    # +1
    next = now + 1
    cost = dist + 1
    if cost < distance[next]:
      distance[next] = cost
      q.append((cost, next))
    # *2
    next = now * 2
    cost = dist + 0
    if cost < distance[next]:
      distance[next] = cost
      q.append((cost, next))

result = HideAndSeek(n, k)
print(result)
  