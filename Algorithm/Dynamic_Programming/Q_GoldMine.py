# 문제명 : 금광
# 문제 : 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m-1번에 걸쳐서 오른쪽위, 오른쪽, 오른쪽아래 3가지 중 하나의 위치로 이동해야 합니다. 이때 채굴자가 얻을 수 있는 금의 최대 크기를 출력하시오.

# 나의 답
# 탑다운 함수
def goldMine(goldMatrix, x, y):
  # 갈 수 없는 길인 경우
  if x < 0 or y < 0 or x >= n or y >= m:
     return -999
  if y == 0: return goldMatrix[x][y]
  if d[x][y] != 0: return d[x][y]
  # 왼쪽위
  a = goldMine(goldMatrix, x-1, y-1)
  # 왼쪽
  b = goldMine(goldMatrix, x, y-1)
  # 왼쪽 아래
  c = goldMine(goldMatrix, x+1, y-1)
  # 가장 큰 값
  d[x][y] = max(a, b, c) + goldMatrix[x][y]
  return d[x][y]

t = int(input())

for test in range(t):
  n, m = map(int, input().split())
  goldMatrix = [[0 for col in range(m)] for row in range(n)]
  data = list(map(int, input().split()))
  count = 0
  # 2차원 배열 초기화
  for i in range(n):
    for j in range(m):
      goldMatrix[i][j] = data[count]
      count += 1
  # DP 테이블
  d = [[0 for col in range(m)] for row in range(n)]
  # 처음에는 n만큼 다 돌려줘야 함
  result = -999
  for i in range(n):
    goldMine(goldMatrix, i, m-1)
    result = max(result, d[i][m-1])
  # 가장 큰 값
  print(result)

###################################################
# 이코테 답

# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
  # 금광 정보
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  #다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(data[index:index+m])
    index += m
  # 다이나믹 프로그래밍 진행
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i==0: left_up = 0
      else: left_up = dp[i-1][j-1]
      #왼쪽 아래에서 오는 경우
      if i==n-1: left_down = 0
      else: left_down = dp[i+1][j-1]
      #왼쪽에서 오는 경우
      left = dp[i][j-1]
      dp[i][j] = dp[i][j]+ max(left_up, left_down, left)
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  print(result)

# 세 가지 방식 중에 비교 => max
# 만약 m번째 열에 도착하면 끝 
# DP 테이블 = N x M
# 갈 수 없는 길 고려
