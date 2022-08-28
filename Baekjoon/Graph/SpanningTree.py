# [최소 스패닝 트리]
# 1197번
import sys
v, e = map(int, sys.stdin.readline().split())
edges = []
for _ in range(e):
  a, b, c = list(map(int, sys.stdin.readline().split()))
  edges.append((c, a, b))
parent = [i for i in range(v+1)]

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

# 크루스칼
edges.sort()
result = 0
for edge in edges:
  c, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += c

print(result)
    