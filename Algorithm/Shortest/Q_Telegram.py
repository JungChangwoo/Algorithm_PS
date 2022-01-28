# 문제명 : 전보
# 문제 : 어떤 나라에 N개의 도시가 있다. 다른 도시로 전보를 보내고자 할 때는 통로(일방향)가 존재해야 한다. 어느 날 도시 C에서 위급상황이 발생했다. 이때 도시 C에서 보낸 메세지를 받게 되는 도시의 개수는 총 몇 개이며, 도시들이 모두 메세지를 받는 데까지 걸리는 시간은 얼마인지를 구하시오.
# 시간 복잡도 
# - 도시 개수 : 1 <= N <= 30,000
# - 통로 개수 : 1 <= M <= 200,000
# - 시간 제한 : 1초
# => Log 이하의 알고리즘을 작성해야 할 것 같다.

# 나의 답

n, m, start = map(int, input().split())

# 무한
INF = int(1e9)
# 그래프
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 간선 입력 받기
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 다익스트라
import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
# 다익스트라 수행
dijkstra(start)

# 결과 출력
totalCity = 0
max_value = 0
for i in range(1, n+1):
  if distance[i] != INF:
    totalCity += 1
    if distance[i] > max_value:
      max_value = distance[i]

# 결과 출력
print(totalCity-1, max_value)

