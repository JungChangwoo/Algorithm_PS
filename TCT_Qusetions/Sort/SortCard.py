# [카드 정렬하기]
# 난이도: 중상
# 권장 풀이 시간: 30분
# 시간 제한: 2초
import heapq
n = int(input())
data = []
for i in range(n):
  heapq.heappush(data, int(input()))

# 가장 작은 두 묶음이 되어야 하며 시간 복잡도는 O(NlogN) 이하여야 한다.
result = 0
part = 0
for i in range(n-1):
  left = heapq.heappop(data)
  right = heapq.heappop(data)
  part = left + right
  result += part 
  heapq.heappush(data, part)
  
print(result)