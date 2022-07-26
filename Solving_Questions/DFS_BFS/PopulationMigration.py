# [인구 이동]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 2초
import sys
n, l, r = map(int, input().split())
graph = []
for i in range(n):
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  graph.append(data)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS(x, y, index):
  count = 1
  sum_value = 0
  union[x][y] = index
  united = []
  united.append((x, y))
  sum_value += graph[x][y]
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    # 4방향으로 진행
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if union[nx][ny] == -1:
          difference = abs(graph[x][y] - graph[nx][ny])
          # 만약, LR 조건에 부합되면 연합에 추가
          if l <= difference and difference <= r:
            union[nx][ny] = index
            united.append((nx, ny))
            q.append((nx, ny))
            count += 1
            sum_value += graph[nx][ny]
  if count != 1:
    # 연합에 속한 국가들 평균내기
    for x, y in united:
      graph[x][y] = sum_value // count

result = 0
while True:
  union = [[-1] * n for _ in range(n)]
  index = 0
  # 모든 나라를 돌면서 인구이동(BFS)
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        BFS(i, j, index)
        index += 1
  if index == n * n:
    break
  result += 1

print(result)
# 1. 모든 나라를 돌면서 BFS (만약, 연합되지 않았다면)
# 1-1. BFS 방식으로 4방향으로 진행하면서, L, R 조건에 부합되면 연합에 추가
# 1-2. 연합에 속한 국가들 평균내기
