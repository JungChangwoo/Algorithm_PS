# [팰린드롬 분할]
# 1509번
import sys
data = list(sys.stdin.readline().rstrip())
n = len(data)
is_p = [[0] * n for _ in range(n)]

def is_palindrom():
  for num in range(n):
    for start in range(n-num):
      end = start + num
      if start == end:
        is_p[start][end] = 1
      elif data[start] == data[end]:
        if end - start == 1:
          is_p[start][end] = 1
        else:
          if is_p[start+1][end-1] == 1:
            is_p[start][end] = 1

is_palindrom()

dp = [2500] * n
dp[0] = 1
for end in range(1, n):
  dp[end] = dp[end-1] + 1 # 이전의 값에 단일 분할로 추가되는 경우로 초기화 (최악의 상황)
  for start in range(end):
    if is_p[start][end] == 1:
      if start == 0: # 만약, 처음부터 끝까지가 Palindrom이라면 바로 정답 
        dp[end] = 1
        break
      dp[end] = min(dp[end], dp[start-1] + 1) # 이전까지의 최소 갯수에 하나를 더해줌
print(dp[-1])
