# [다익스트라 최단 경로 알고리즘]
# : 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.
# [조건]
# - 음의 간선이 없을 때 정상적으로 동작
# [특징]
# - 그리디 알고리즘으로 분류됨 
# - 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바꾸지 않는다. (한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다)
# - 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다. (완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 한다)
# [동작 과정]
# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 위 과정에서 3번 4번 반복
# [간단한 구현]

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억으로 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(n):
  a, b, c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용 c
  graph[a].append((b,c))

# 반문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드 (인덱스)
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost 

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한(INF)이라고 출력
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])

# [간단한 구현 방법 성능 분석]
# - 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 합니다.
# - 따라서 전체 시간 복잡도는 O(V^2) 
# - 일반적으로 코딩 테스트 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 알고리즘으로 해결할 수 있다.

# [개선된 구현 방법 (Heap사용)]
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미
# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(n):
  a, b, c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용 c
  graph[a].append((b,c))


def dijkstra2(start):
  q = []
  # 시작 노드에 대해서 초기화
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: #큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (아직 뽑지 않았는데, 더 최적의 값으로 갱신되는 과정에서 같은 노드가 여러 개 들어갈 수 있음)
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra2(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])
    
# [개선된 구현 방법 성능 분석]
# 시간 복잡도 : O(ElogV)
# 노드를 하나씩 꺼내 검사하는 반복문 (while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않는다. (결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있다)
# 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다.
# - 시간 복잡도를 O(ElogE)로 판단할 수 있다.
# - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있다.
# => O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV)
# ( E <= V^2 )

