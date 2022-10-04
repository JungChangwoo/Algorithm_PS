# [최대 힙]
# 11279번
import sys
import heapq
n = int(sys.stdin.readline().rstrip())
q = []
for _ in range(n):
  data = int(sys.stdin.readline().rstrip())
  if data == 0:
    if len(q) == 0:
      print(0)
    else:
      print(-heapq.heappop(q))
  heapq.heappush(q, -data)

