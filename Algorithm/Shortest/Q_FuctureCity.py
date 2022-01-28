# 문제명 : 미래 도시
# 문제 : 미래 도시에는 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로(양방향)를 통해 연결되어 있다. 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다. 이때 A가 K번 회사를 방문한 뒤에 X번 회사로 가는 최소 시간을 계산하는 프로그램을 작성하시오. (통로 시간 : 1)
# 시간 복잡도
# - 회사 개수 : 1 <= N <= 100
# - 경로 개수 : 1 <= M <= 100
# - 시간 제한 : 1초
# => N의 3제곱도 괜찮아 보인다.

# 나의 답 
n, m = map(int, input().split())

# 무한
INF = int(1e9)
# 그래프
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(n+1):
  for b in range(n+1):
    if a==b: graph[a][b] = 0

# 간선 입력 받기
for i in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1
# X, K 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘을 수행
for j in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b] ,graph[a][j] + graph[j][b])

# 결과 출력
result = graph[1][k] + graph[k][x]
if result >= INF:
  print(-1)
else:
  print(result)

# [배운 점]
# 중간을 거쳐서 가는 방법을 찾을 때 특별한 생각보다는 a -> k 까지의 최적 + k -> x 까지의 최적
# => 반례가 없는지 잘 생각 => 없다면 GO