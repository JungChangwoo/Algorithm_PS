# [연결 요소의 개수]
# 11724번
import sys

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

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  edges.append((a, b))

parent = [i for i in range(n+1)]
for edge in edges:
  a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)

result = 0
for i in range(1, len(parent)):
  if i == parent[i]:
    result += 1
print(result)