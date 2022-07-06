# [자물쇠와 열쇠]
#잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
#자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
#열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# key는 M x M (3 <= M <= 20) 크기 2차원 배열입니다.
# lock은 M x M (3 <= N <= 20) 크기 2차원 배열입니다.
# M은 항상 N 이하입니다. 
# 시간 제한 : 1초
# 메모리 제한 : 128MB

def rotate_a_matrix_by_90_degree(a):
  n = len(a)
  m = len(a[0])
  result = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

def check_lock(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  new_lock = [[0] * (n*3) for _ in range(n*3)]
  for i in range(n):
    for j in range(n):
      new_lock[i + n][j + n] = lock[i][j]

  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    for x in range(n*2):
      for y in range(n*2):
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] += key[i][j]
        if check_lock(new_lock) == True:
          answer = True
          return answer
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]
  return False

# [문제 해결 아이디어]
# 1. 완전 탐색
# 2. 테이블 확장 (덧대기)