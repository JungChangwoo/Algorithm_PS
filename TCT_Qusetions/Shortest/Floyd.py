# [플로이드]
# n 개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다. 모든 도시의 쌍 (A, B)에 대해서 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
# (1 <= n <= 100)
# (1 <= m <= 100,000)
# 시간 제한 : 1초

n = int(input())
m = int(input())

INF = (1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(c, graph[a][b])

for i in range(n+1):
  for j in range(n+1):
    if i==j:
      graph[i][j] = 0

# 플로이드 수행
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    # 도달할 수 없는 경우, 0을 출력
    if graph[i][j] == INF:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()
