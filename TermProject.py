# [텀 프로젝트]
# 9466번
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
    count[a][0] += 1
  else:
    parent[a] = b
    count[b][0] += 1

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  n = int(sys.stdin.readline().rstrip())
  parent = [i for i in range(n+1)]
  edges = []
  data = list(map(int, sys.stdin.readline().split()))
  for i in range(n):
    edges.append((i+1, data[i]))

  result = 0
  count = [[0,0] for _ in range(n+1)]
  for edge in edges:
    a, b = edge
    # 만약 자기 자신을 선택했다면 
    if a == b:
      continue
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
    # 만약, 부모가 같은데 연결을 했다면 팀
    else:
      parentIdx = find_parent(parent, a)
      count[parentIdx][0] += 1
      count[parentIdx][1] = 1
  for i in range(1, n+1):
    if count[i][1] == 0:
      result += count[i][0]
  print(result)
