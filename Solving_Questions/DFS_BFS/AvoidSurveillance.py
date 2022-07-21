# [감시 피하기]
# 난이도: 상
# 권장 풀이 시간: 60분
# 시간 제한: 2초

n = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
teachers = []
stuff = []
for i in range(n):
  data = list(input().split())
  graph.append(data)
  for j in range(n):
    if data[j] == 'T':
      teachers.append((i, j))
    elif data[j] == 'X':
      stuff.append((i, j))

# 모든 경우의 수 중에서 3개를 선택하는 조합을 획득
from itertools import combinations
cases = list(combinations(stuff,3))

# 선생님이 상, 하, 좌, 우로 확인
def watch(graph, x, y):
  # 상, 하, 좌, 우 확인
  for i in range(4):
    nx = x
    ny = y
    direction = i
    while True:
      nx = nx + dx[direction]
      ny = ny + dy[direction]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
      elif graph[nx][ny] == 'O':
        break
      elif graph[nx][ny] == 'S':
        return False
  return True

import copy
result = False
# 조합을 돌면서 가능한지 확인
for case in cases:
  # 장애물 설치
  temp_graph = copy.deepcopy(graph)
  for i in range(3):
    x, y = case[i]
    temp_graph[x][y] = 'O'
  case_result = True
  # 선생님을 돌아가면서 가능한지 확인
  for teacher in teachers:
    x, y = teacher
    if watch(temp_graph, x, y) == False:
      case_result = False
  # 모든 선생님이 조건에 만족한다면
  if case_result == True:
    result = True
    
if result == True:
  print('YES')
else:
  print('NO')
    
# 모든 경우의 수 중에 3개를 선택하는 조합을 획득
# 모든 조합을 돌면서 가능한지 확인 (장애물 True 학생 False)