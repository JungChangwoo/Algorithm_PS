# [계단 수]
# 1562번
import sys
n = int(sys.stdin.readline().rstrip())
MOD = 1000000000

def Numstair():
  dp = [[0 for _ in range(1024)] for _ in range(10)]
  # 길이 1 처리
  for i in range(1, 10):
    dp[i][1 << i] = 1
    
  # 길이
  for _ in range(2, n):
    next_dp = [[0 for _ in range(1024)] for _ in range(10)]
    # 마지막 숫자
    for end in range(10):
      # 집합
      for bm in range(1024):
        # 현재까지의 집합의 경우의 수에 마지막 숫자가 포함된 집합의 경우의 수를 더해줌
        if end < 9:
          next_dp[end][bm | (1 << end)] = (next_dp[end][bm | (1 << end)] + dp[end+1][bm]) % MOD
        if end > 0:
          next_dp[end][bm | (1 << end)] = (next_dp[end][bm | (1 << end)] + dp[end-1][bm]) % MOD
    dp = next_dp
  return sum(dp[i][1023] for i in range(10)) % MOD

print(Numstair())
