# [행성 터널]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 1초
# 메모리 제한: 128MB 

n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

planets = []
for i in range(n):
  x, y, z = map(int, input().split())
  planets.append((x, y, z))

edges = []
for i in range(n-1):
  for j in range(i+1, n):
    a = planets[i]
    b = planets[j]
    cost = min(abs(a[0]- b[0]), abs(a[1]- b[1]), abs(a[2]- b[2]))
    edges.append((cost, i, j))

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

result =0
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
    