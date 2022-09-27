# // 개선된 LCA 알고리즘 //
# "모든 노드에 대하여 2^i 번째 부모에 대한 정보를 계산"
# 시간 복잡도: O(logN)
import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)
level = [0] * (n+1)
LOG = 21 # LOG 20 = 1,000,000
parent = [[0] * 21 for _ in range(n+1)]
def DFS(now, depth):
  visited[now] = True
  level[now] = depth
  for next in graph[now]:
    if not visited[next]:
      parent[next][0] = now
      DFS(next, depth + 1)

def set_parent():
  DFS(1, 0)
  for j in range(1, LOG):
    for i in range(1, n+1):
      parent[i][j] = parent[parent[i][j -1]][j-1]

def LCA(a, b):
  # b가 더 깊도록 설정
  if level[a] > level[b]:
    a, b = b, a
  # 깊이가 같아지도록 설정
  for i in range(LOG - 1, -1, -1):
    if level[b] - level[a] >= (1 << i):
      b = parent[b][i]
  # 부모가 같아지도록
  if a == b:
    return a
  for i in range(LOG -1, -1, -1):
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]
  return parent[a][0]

set_parent()

m = int(sys.stdin.readline().rstrip())
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(LCA(a, b))
      