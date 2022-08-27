# [뱀과 사다리 게임]
# 16928번
import sys
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (101) for _ in range(101)]

visited = [False] * 101
for _ in range(n+m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = 0
  visited[a] = True
# 자기자신 0 초기화
for i in range(1, 101):
  graph[i][i] = 0

# 간선 초기화(1 ~ 6 이동가능 or 사다리 뱀)
for i in range(1, 101):
  # 만약, 사다리나 뱀이 있다면
  if visited[i] == True:
    continue
  # 주사위 1~6까지 한 번에 이동 가능
  for j in range(1, 7):
    if i + j < 101:
      graph[i][i+j] = 1

# 플로이드 워셜
for k in range(1, 101):
  for a in range(1, 101):
    for b in  range(1, 101):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph[1][100])

