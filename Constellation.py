# [별자리 만들기]
# 4386번
import sys
n = int(sys.stdin.readline().rstrip())
stars = []
for _ in range(n):
  stars.append(list(map(float, sys.stdin.readline().split())))

edges = []
for i in range(n):
  for j in range(n):
    if i==j:
      continue
    cost = ((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5
    edges.append((cost, i, j))

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

parent = [i for i in range(n)]
edges.sort()
result = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
print(round(result, 2))