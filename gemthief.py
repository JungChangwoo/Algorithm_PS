# [벡터 매칭]
# 1007번 
import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
gems = []
for _ in range(n):
  heapq.heappush(gems, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(k):
  bags.append(int(sys.stdin.readline().rstrip()))
bags.sort()

result = 0
values = []
for bag in bags:
  while gems and bag >= gems[0][0]:
    heapq.heappush(values, -heapq.heappop(gems)[1])
  if values:
    result -= heapq.heappop(values)
  elif not gems:
    break

print(result)
