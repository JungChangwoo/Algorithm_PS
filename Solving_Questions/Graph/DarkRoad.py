# [어두운 길]
# 한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다. 모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일합니다. 정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 ㄷ 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 합니다. 결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 합니다. 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하세요.

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

n, m = map(int, input().split())

parent = [i for i in range(n)]
edges = []

total_cost = 0

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  total_cost += cost

edges.sort()

min_cost = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    min_cost += cost

result = total_cost - min_cost
print(result)