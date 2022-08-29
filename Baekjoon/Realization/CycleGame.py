# [사이클 게임]
# 20040번
import sys
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
  edges.append(map(int, sys.stdin.readline().split()))
parent = [i for i in range(n)]

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
    parent[a] =b

def cycle():
  count = 1
  for edge in edges:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
    else:
      return count
    count += 1
  return None

result = cycle()
if result == None:
  print(0)
else:
  print(result)
