# [금광]
# n x m 크기의 금광이 있습니다. m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.

def goldMine(graph, x, y):
  # 그래프에서 벗어날 경우
  if x<0 or x>=n or y<0 or y>=m:
    return -999
  if y == 0: return graph[x][y]
  # 이미 계산됨
  if dp[x][y] != 0:
    return dp[x][y]
  dp[x][y] = max(goldMine(graph, x-1, y-1), goldMine(graph, x, y-1), goldMine(graph, x+1, y-1)) + graph[x][y]
  return dp[x][y]

t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  dp = [[0 for _ in range(m)] for _ in range(n)]

  graph = []
  index = 0
  for i in range(n):
    graph.append(data[index:index+m])
    index += m

  print(dp)
  print(graph)


  result = -999
  for i in range(n):
    goldMine(graph, i, m-1)
    result = max(result, dp[i][m-1])
  # 가장 큰 값
  print(result)


# [다이나믹 재귀적]
# - 예외상황
# - 마지막 탈출 조건
# - 부분 구조
# - dp 테이블과 graph의 일치
