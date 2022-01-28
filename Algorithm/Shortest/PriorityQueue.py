# [우선순위 큐 (Priority Queue)]
# : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# Ex) 여러 개의 데이터를 넣었다가 가치가 높은 물건 데이터를 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있다.
# 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원합니다.
# [힙 (Heap)]
# 우선순위 큐를 구현하기 위해 사용되는 자료구조 중 하나
# <특징>
# 최소 힙(Min_Heap) 최대 힙(Max Heap)
# 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용된다.
# <시간 복잡도>
# - 삽입 시간 O(log N)
# - 삭제 시간 O(log N)

# [힙 라이브러리 사용 예제 : 최소 힙]
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8 ,0])
print(result)
# [힙 라이브러리 사용 예제 : 최대 힙]
import heapq

# 내림차순 힙 정렬 (Heap Sort)
def heapsort2(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, -value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8 ,0])
print(result)