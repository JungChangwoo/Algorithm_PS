# [위상 정렬]
# : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# EX) 선수과목을 고려한 학습 순서 설정
# <특징>
# - DAG(Direct Acyclic Graph)에 대해서만 수행할 수 있다.
# - 여러 가지 답이 존재할 수 있다.
# - 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
# - 스택을 활용한 DFS를 이용해 수행할 수도 있다.
# <동작 과정>
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
# 2-1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
# 2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# <간단한 구현>

from collection import deque

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # 정점 A에서 B로 이동 가능
  # 진입 차수를 1증가
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque()
  # 처음 시작할 때
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
    # 위상정렬을 수행한 결과 출력 
  for i in result:
    print(i, end=' ')

topology_sort()