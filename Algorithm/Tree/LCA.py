# [최소 공통 조상 (LCA, Lowest Common Ancestor)]
# "트리 구조에서 임의의 두 정점이 갖는 가장 가까운 조상 정점"

# // 선형 탐색으로 구하기: O(Depth) //
# => O(logN) => 최악의 경우 O(N)
# : 두 포인터를 두고 가리키는 정점이 같아질 때까지 부모 노드로 거슬러 올라감
# But, level이 다르면 문제 발생
# => 두 노드의 level을 맞춰둔 뒤 선형탐색

# [LCA (11437번)]
import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

level = [0] * (n+1)
visited = [False] * (n+1)
parent = [0] * (n+1)

# DFS로 탐색하며 깊이와 부모를 알아낸다.
def DFS(now, depth):
  visited[now] = True
  level[now] = depth
  for next in graph[now]:
    if not visited[next]:
      parent[next] = now
      DFS(next, depth + 1)

def LCA(a, b):
  # 두 노드의 level을 맞춰준다.
  while level[a] != level[b]:
    if level[a] > level[b]:
      a = parent[a]
    else:
      b = parent[b]
  # 두 노드가 같아지
  while a != b:
    a = parent[a]
    b = parent[b]
  return a
      
DFS(1, 0)
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(LCA(a, b))