# 각 줄 확인
# 값이 같다면 움직임
# 값이 같지 않다면 경사로 확인
# 무사히 다 움직였다면 True
n, l = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

  
def check(line, incline):
  for i in range(n-1):
    now = line[i]
    next = line[i + 1]
    # 값이 2이상 차이나면 불가능
    if abs(now - next) > 1:
      return False
    # 값이 같으면 계속 진행
    if now == next:
      continue
    # 값이 1만큼 차이나고 다음 값이 더 크다면 왼쪽으로 경사로 놓음
    if now < next:
      for j in range(l):
        # 왼쪽 범위 벗어남 or 값이 다름 or 이미 경사로 놓임
        if now - j < 0 or line[now] != line[now - j] or incline[now - j]:
          return False
        else:
          incline[now-j] = True
    # 오른쪽으로 경사로 놓음 2 1
    if now > next:
      for j in range(l):
        # 오른쪽 범위 벗어남 or 값이 다름 or 이미 경사로 놓임
        if next + j >= n or line[next] != line[next + j] or incline[next + j]:
          return False
        else:
          incline[next + j] = True
  return True
    
  
result = 0
# 가로
for i in range(n):
  incline = [False] * n
  line = [graph[i][j] for j in range(n)]
  if check(line, incline):
    result += 1
# 세로
for j in range(n):
  incline = [False] * n
  line = [graph[i][j] for i in range(n)]
  if check(line, incline):
    result += 1
