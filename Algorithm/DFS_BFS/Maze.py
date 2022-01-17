# 문제명 : 미로 탈출
# 문제 : 괴물을 피해서 미로를 탈출할 수 있는 최적의 경로를 찾으시오.
from collections import deque
# 입력 처리
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def BFS(x, y):
  queue = deque()
  queue.append((x,y))
  while queue:
     x,y = queue.popleft()
     # 현재 위치로부터 4가지 방향 확인
     for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 벗어난 범위
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      # 괴물 확인
      if graph[nx][ny]==0:
        continue
      # 처음 방문일 때
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  for i in range(n):
    print(graph[i])
  return graph[n-1][m-1]
print(BFS(0, 0))

######################################################배운 점
# 처음 방문일 때 최단 경로를 설정해줬을 때, 뒤 순서로 방문한 더 최적의 경로가 있으면 안 되지 않나? 라고 생각했지만, 현재 문제 조건은 Queue가 돌 때 마다 한 칸 씩 움직이기 때문에, 더 늦게 도착한 경로가 더 최적인 경로가 될 수 없음