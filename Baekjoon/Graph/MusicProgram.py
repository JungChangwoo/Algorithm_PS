# [음악프로그램]
# 2623번
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
in_count = [0] * (n+1)
for _ in range(m):
  data = list(map(int, sys.stdin.readline().split()))
  for i in range(1, len(data) - 1):
    a, b = data[i], data[i+1]
    graph[a].append(b)
    in_count[b] += 1

from collections import deque
def musicprogram():
  count = 0
  q = deque()
  for i in range(1, n+1):
    if in_count[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    count += 1
    for next in graph[now]:
      in_count[next] -= 1
      if in_count[next] == 0:
        q.append(next)
  if count < n:
    return False
  else:
    return True

result = []
if musicprogram():
  for i in result:
    print(i)
else:
  print(0)