# [벡터 매칭]
# 1007번 
import sys
n, k = map(int, sys.stdin.readline().split())
gems = []
for _ in range(n):
  gems.append(list(map(int, sys.stdin.readline().split())))
back = []
for _ in range(k):
  back.append(int(sys.stdin.readline().rstrip()))

gems.sort(reverse=True, key = lambda x: x[1])
back.sort()

INF = int(1e9)

def binary_search(array, target, start, end):
  if start > end:
    return start
  mid = (start+end) // 2
  if array[mid] == target:
    return mid
  if array[mid] < target:
    return binary_search(array, target, mid+1, end)
  else:
    return binary_search(array, target, start, mid-1)  
    
# 보석을 높은 가치순으로 돈다.
result = 0
for gem in gems:
  if len(back) == 0:
    break
  m, v = gem
  # 보석을 담을 수 있는 가방 중에서 가장 작은 가방 선택
  idx = binary_search(back, m, 0, len(back)-1)
  # 담을 수 있는 가방이 없다면 pass
  if idx == len(back):
    continue
  else:
    result += v
    back[idx] = INF

print(result)

# 최적 조건: 작은 가방에 높은 가치의 보석이 담겨야 한다.
# 1. 높은 가치순으로 보석을 돈다.
# 2. 해당 보석을 담을 수 있는 가방 중에서 가장 작은 가방 선택(시간 1 or log)
