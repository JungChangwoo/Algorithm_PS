# [이중 우선순위 큐]
# 7662번
import sys
import heapq

for _ in range(int(sys.stdin.readline().rstrip())):
  k = int(sys.stdin.readline().rstrip())
  min_heap = []
  max_heap = []
  count_I = 0
  count_D = 0
  dict = {}
  for _ in range(k):
    oper, value = sys.stdin.readline().split()
    value = int(value)
    if oper == 'I':
      count_I += 1
      heapq.heappush(min_heap, value)
      heapq.heappush(max_heap, -value)
      if dict.get(value):
        dict[value] += 1
      else:
        dict[value] = 1
        
    else:
      if value == 1:
        while max_heap:
          temp = -heapq.heappop(max_heap)
          if dict[temp] > 0:
            dict[temp] -= 1
            break
      else:
        while min_heap:
          temp = heapq.heappop(min_heap)
          if dict[temp] > 0:
            dict[temp] -= 1
            break
  result = []
  for key, value in dict.items():
    if value > 0:
      result.append(key)
  if len(result) > 0:
    result.sort()
    print(result[-1], result[0])
  else:
    print('EMPTY')
  