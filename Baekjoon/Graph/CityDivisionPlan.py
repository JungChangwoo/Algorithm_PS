# [도시 분할 계획]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 2초

import sys
n, m = map(int, input().split())
edges = []
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  edges.append((c, a, b))
edges.sort()

parent = [i for i in range(n+1)]

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

result = 0
max_cost = 0
count = 0
# 가장 작은 간선부터 연결
for edge in edges:
  cost, a, b = edge
  # 이미 연결되어 있지 않다면 연결
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    max_cost = cost
    count += 1
  # 모든 정점이 연결되었다면
  if count == n-1:
    break

print(result - max_cost)
