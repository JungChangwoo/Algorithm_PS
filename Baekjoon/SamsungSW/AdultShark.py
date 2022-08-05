# [어른 상어]
# 19237번

import sys
n, m, k = map(int, input().split())

array = []
for i in range(n) :
  array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0, 0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m) :
  for j in range(4) :
    priorities[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell() :
  for i in range(n) :
    for j in range(n) :
      if smell[i][j][1] > 0 :
        smell[i][j][1] -= 1
      if array[i][j] != 0 :
        smell[i][j] = [array[i][j], k]


def move() :
  new_array = [[0] * n for _ in range(n)]
  # 각 위치를 하나씩 확인하며
  for x in range(n) :
    for y in range(n) :
      # 상어가 존재하는 경우
      if array[x][y] != 0 :
        direction = directions[array[x][y] - 1] # 현재 상어의 방향
        found = False
        # 일단 냄새가 존재하지 않는 곳이 있는지 확인
        for index in range(4) :
          nx = x + dx[priorities[array[x][y] - 1][direction-1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction-1][index] - 1]
          if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if smell[nx][ny][1] == 0 : # 냄새가 존재하지 않는 곳이면
              # 해당 상어의 방향 이동시키기
              directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction-1][index]
              # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
              # 상어 이동시키기
              if new_array[nx][ny] == 0 :
                new_array[nx][ny] = array[x][y]
              else :
                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
              found = True
              break
        if found :
          continue
        # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
        for index in range(4) :
          nx = x + dx[priorities[array[x][y] - 1][direction-1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction-1][index] - 1]
          if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if smell[nx][ny][0] == array[x][y] : # 자신의 냄새가 있는 곳이면
              # 해당 상어의 방향 이동시키기
              directions[array[x][y] - 1] = priorities[array[x][y]-1][direction-1][index]
              # 상어 이동 시키기
              new_array[nx][ny] = array[x][y]
              break
  return new_array


time = 0
while True :
  update_smell() 
  new_array = move() 
  array = new_array
  time += 1
  
  # 1번 상어만 남았는지 체크
  check = True
  for i in range(n) :
    for j in range(n) :
      if array[i][j] > 1 :
        check = False
  
  if check :
    print(time)
    break
  
  # 1,000초가 지날 때까지 끝나지 않았다면
  if time >= 1000 :
    print(-1)
    break