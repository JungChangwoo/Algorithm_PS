# [특정 거리의 도시 찾기]
# 어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재합니다. 모든 도로의 거리는 1입니다. 어떤 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서 최단 거리가 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.
# (2<= N <=300,000) (1<= M <=1,000,000) (1<= K <=300,000)
# 시간제한 : 2초

# 나의 답
n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

visited = [False] * (n+1)

count = [0] * (n+1)
result = []

from collections import deque
def BFS(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        count[i] = count[v] + 1
BFS(graph, 1, visited)

print(count)

for i in range(1, len(count)):
  if count[i] == k:
    result.append(i)

if len(result) == 0:
  print(-1)
else:
  for i in result:
    print(i, end=' ')
