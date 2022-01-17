# 문제 : 게임 개발
# 조건 : 반시계 방향으로 돌면서 갈 수 있는 곳인지 확인하여 반복함. 이때, 사면이 모두 이미 가본 칸이거나 바다로 되어 있는 경우에는, 뒤로 1칸 움직이고 처음부터 반복 (뒤가 바다인 칸이라 갈 수 없는 경우에 멈춤)

# 입력 설정
row, column = map(int, input().split())
x, y, d = map(int, input().split())
myMap = []
for i in range(row):
  myMap.append(list(map(int, input().split())))

# 시작 지점 처리
myMap[x][y] = 2

# 방향 벡터
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1] # 북동남서

# 반시계 방향 회전
def turn_left(d):
  d -= 1
  if d == -1: d = 3
  return d

count = 0
result = 1

while True:
  # 1. 현재 위치에서 반시계 방향으로 회전
  d = turn_left(d)
  # 2. 한 칸 전진 (만약, 갈 수 없다면 1단계로 돌아감)
  nx = x + dx[d]
  ny = y + dy[d]
  if myMap[nx][ny] == 0: # 갈 수 있다면
    myMap[nx][ny] = 2 # 방문 처리
    x, y = nx, ny
    count = 0
    result += 1
    continue
  else:
    count += 1
  # 3. 네 방향 모두 갈 수 있는 곳이 없을 때, (방향유지 및 뒤로 한 칸)
  if count == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    if myMap[nx][ny] == 1:
      break
    x, y = nx, ny
    myMap[x][y] = 2
    count = 0
    result += 1

print(result)

#################################################################### 배운 점
# 함수를 사용하면 코드 보기가 편하다
# 반대 방향이라고 하면 그냥 + => - 로 해주면 된다.
# 2차원 배열에 익숙해지자