# [분기 한정]
# 일반적인 방법으로는 BFS가 DFS보다 좋은 점이 없다.
# => 유망 함수 외에 추가적으로 한계값을 사용
# 1. 자식 노드 방문
# 2. 유망하면서 확장하지 않은 노드들을 확인
# 3. 그 중에서 한계값이 가장 좋은 노드를 우선적으로 확장
# "우선선위 큐를 활용한 BFS"

import heapq
q = []
data = [4, 1, 3, 2]
for i in range(len(data)):
  heapq.heappush(q, data[i])
while q:
  print(heapq.heappop(q))


