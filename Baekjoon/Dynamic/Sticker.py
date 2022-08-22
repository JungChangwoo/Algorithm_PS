# [스티커]
# 9465번
import sys
T = int(sys.stdin.readline().rstrip())
def DFS(x, y, value):
  # 오른쪽 끝에 도달했다면 return
  if y > n-1:
    return 0
  # 오른쪽 끝에 도달했다면 return
  if y == n-1:
    dp[x][y] = graph[x][y]
    return dp[x][y]
  # 만약, 이미 계산된 값이라면
  if dp[x][y] != 0:
    return dp[x][y]
  # 윗 줄이라면, ㄴ의 형태로 DFS
  if x == 0:
    value1 = DFS(x+1, y+1, value)
    value2 = DFS(x+1, y+2, value)
    dp[x][y] = max(value1, value2) + graph[x][y]
    return dp[x][y]
  # 아랫 줄이라면, ㄱ의 형태로 DFS
  if x == 1:
    value1 = DFS(x-1, y+1, value)
    value2 = DFS(x-1, y+2, value)
    dp[x][y] = max(value1, value2) + graph[x][y]
    return dp[x][y]
    
for _ in range(T):
  n = int(sys.stdin.readline().rstrip())
  dp = [[0] * n for _ in range(2)]
  result = 0
  graph = []
  for _ in range(2):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
  # 처음 시작하는 두 가지 경우의 수로 DFS
  dp[0][0] = graph[0][0]
  dp[1][0] = graph[1][0]
  if n >= 2:
    dp[0][1] = graph[0][1] + graph[1][0]
    dp[1][1] = graph[1][1] + graph[0][0]
  for j in range(2, n):
    for i in range(2):
      if i == 0:
        dp[i][j] = max(dp[i+1][j-1], dp[i+1][j-2]) + graph[i][j]
      else:
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + graph[i][j]
  
  print(max(dp[0][n-1], dp[1][n-1]))



# 뗄 수 있는 스티커 점수의 최댓값
# 1. 변을 공유하지 않는다.
# 2. 점수의 합이 최대

# 1. DFS로 조합을 텀색
# 1-1. 주위를 제외한 나머지를 DFS
# 1-2. 만약 범위를 벗어나면 global result와 비교 후 return
# 1-3. dynamic 있다면 바로 return 없다면 DFS
