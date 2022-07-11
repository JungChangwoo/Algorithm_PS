# [뱀]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 1초
# 메모리 제한: 128MB

n = int(input())
k = int(input())

myMap = [[0 for _ in range(n)] for _ in range(n)]

for i in range(k):
  i, j = map(int, input().split())
  myMap[i-1][j-1] = 2

l = int(input())
da = []
for i in range(l):
  count, d = input().split()
  da.append((int(count), d))

dx = [0, 1, 0, -1] #우, 하, 좌, 상
dy = [1, 0, -1, 0] 

d = 0

# 반시계 방향 회전
def turn_left(d):
  d -= 1
  if d == -1: d = 3
  return d

# 시계 방향 회전
def turn_right(d):
  d += 1
  if d == 4: d = 0
  return d

def check_direction(count, d):
  for i in da:
    if count == i[0]:
      if i[1] == 'D':
        return turn_right(d)
      else:
        return turn_left(d)
  return d
  
x, y = 0, 0
myMap[x][y] = 1
visited = []
visited.append((x, y))
count = 0

while True:
  count += 1
  # 이동
  nx = x + dx[d]
  ny = y + dy[d]
  # 몸에 부딪히거나 벽에 부딪혔을 때 게임 종료
  if nx < 0 or ny < 0 or nx >= n or ny >= n:
    break;
  if myMap[nx][ny] == 1:
    break;
  #실제 이동
  x, y = nx, ny 
  # 사과를 안 먹었다면 꼬리 자르기
  if myMap[nx][ny] != 2:
    tailX, tailY = visited.pop(0)
    myMap[tailX][tailY] = 0
    myMap[x][y] = 1
    visited.append((x, y))
  else:
    myMap[x][y] = 1
    visited.append((x, y))

  # 방향 체크
  d = check_direction(count, d)

  print(visited)


print(count)