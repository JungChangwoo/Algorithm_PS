# [정수 삼각형]
# 1932번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = []
for i in range(1, n+1):
  dp.append([0] * i)

def DFS(x, y):
  # 만약 마지막에 도달했다면 return
  if x == n - 1:
    return graph[x][y]
  # 이전에 계산된 값이라면
  if dp[x][y] != 0:
    return dp[x][y]
  # 이전 계산된 값이 아니라면
  else:
    dp[x][y] = max(DFS(x+1, y), DFS(x+1, y+1)) + graph[x][y]
    return dp[x][y]

print(DFS(0, 0))