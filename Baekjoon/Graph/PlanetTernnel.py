# [행성 터널]
# 2887

import sys
n = int(sys.stdin.readline().rstrip())
planets = []
x, y, z = [], [], []
for i in range(n):
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  planets.append(data)
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))
x.sort()
y.sort()
z.sort()

# 모든 간선을 구함 (x, y, z)
edges = []
for i in range(n-1):
  edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
  edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
  edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

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
    parent[a] = b

# 가장 작은 간선부터 모든 간선을 확인하며 터널을 연결
result = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)