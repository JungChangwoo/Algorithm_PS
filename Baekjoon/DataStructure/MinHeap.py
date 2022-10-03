# [최소 힙]
# 1927번
import heapq
import sys
n = int(sys.stdin.readline().rstrip())
q = []
for _ in range(n):
  data = int(sys.stdin.readline().rstrip())
  if data == 0:
    if len(q) == 0:
      print(0)
    else:
      print(heapq.heappop(q))
  else:
    heapq.heappush(q, data)
