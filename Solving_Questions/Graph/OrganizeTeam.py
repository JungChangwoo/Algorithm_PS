# [팀 결성] Chapter 2
# 난이도: 중상
# 권장 풀이 시간: 20분
# 시간 제한: 2초

n, m = map(int, input().split())
datas = []
for i in range(m):
  datas.append(list(map(int, input().split())))

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

parent = [i for i in range(n+1)]

for data in datas:
  operate, a, b = data
  if operate == 0:
    union_parent(parent, a, b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')