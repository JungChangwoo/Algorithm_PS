# [여행 계획]
# 한울이가 사는 나라에는 N개의 여행지가 있다. 임의의 두 여행지 사이에는 연결하는 도로가 존재할 수 있다. 이때, 도로는 양방향으로 이동이 가능하다. 한울이가 어떤 순서대로 여행지를 방문하고자 할 때, 해당 계획이 가능한지의 여부를 판별하는 프로그램을 작성하시오.
# (1 <= N,M <= 500)
# 시간 제한 : 1초

# 나의 답
n, m = map(int, input().split())

graph = [] 
for i in range(n):
  graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

parent = [0] * (n) # 부모 테이블 초기화
edges = []

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
  parent[i] = i

# 모든 도로에 대한 정보를 입력받기
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      edges.append((i, j))

# 신장트리 완성
for edge in edges:
  a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)

# 여행 계획 가능한지 확인
result = True
for i in range(m-1):
  if find_parent(parent, plan[i] -1) != find_parent(parent, plan[i+1] -1):
    result = False

if result:
  print('YES')
else:
  print('NO')

# [회고]
# - 정점들 간에 연결이 되는지를 확인하고 싶을 때는 신장트리(크루스칼) 알고리즘을 사용하면 간편하다