import sys
def dfs(x, y, count, visited):
  global result
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < r and 0 <= ny < c:
      if not visited[ord(graph[nx][ny]) - 65]:
        visited[ord(graph[nx][ny]) - 65] = True
        dfs(nx, ny, count + 1, visited)
        visited[ord(graph[nx][ny]) - 65] = False
  
  result = max(result, count)
        
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

visited = [False] * 26
visited[ord(graph[0][0]) - 65] = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 1
dfs(0, 0, 1, visited)
print(result)
# 1. 상하좌우로 이동한다.
# 2. visited에 포함되는지 확인
