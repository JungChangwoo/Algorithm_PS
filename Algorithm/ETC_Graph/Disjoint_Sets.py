# [서로소 집합 (Disjoint Sets)]
# <서로소 집합 자료구조>
# : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# - 합집합(Union) : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# - 찾기(Find) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# - 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도 한다.

# <기본적인 구현 방법>
# => 관행적으로 큰 쪽에 작은 쪽으로 Union
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end = ' ')
for i in range(1, v+1):
  print(find_parent(parent, i), end = ' ')
print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end = ' ')
for i in range(1, v+1):
  print(parent[i], end = ' ')

# <기본적인 구현 방법의 문제점>
# - 합집합(Union) 연산이 편향되게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작
# - 최악의 경우에는 찾기(Find) 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)

# <서로소 집합 자료구조: 경로 압축>
# : 찾기(Find) 함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용
# => 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신
def find_parent_pathCompression(parent, x):
  if parent[x] != x:
    parent[x] = find_parent_pathCompression(parent, parent[x])
  return parent[x]

# <서로소 집합을 활용한 사이클 판별>
# - 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있습니다.
# (참고로 방향 그래프에서의 사이클 여부는 DFS를 이용해서 판별 가능)
# - 사이클 판별 알고리즘은 다음과 같다.
# 1. 각 간선을 하나씩 확인하여 두 노드의 루트 노드를 확인한다. 
# 1-1) 루트 노드가 서로 다르다면 두 노드에 대해 합집합 연산 수행
# 1-2) 루트 노드가 서로 같다면 사이클(Cycle) 발생한 것 
# 2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복

# <서로소 집합을 활용한 사이클 판별>
cycle = False # 사이클 발생 여부

for i in range(e):
  a, b = map(int, input().split())
  # 사이클이 발생한 경우 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행 
  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")
