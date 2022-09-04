# [팰린드롬?]
# 10942번
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

#dp
dp = [[0] * n for _ in range(n)]
for num in range(n):
  for start in range(n-num):
    end = start + num
    # 원소가 하나라면 무조건 성립
    if start == end:
      dp[start][end] = 1
    # 처음과 끝이 같다면
    elif array[start] == array[end]:
      # 원소가 두 개라면 무조건 성립
      if end - start == 1:
        dp[start][end] = 1
      else:
        # 만약, 가운데의 범위가 성립한다면 성립
        if dp[start+1][end-1] == 1:
          dp[start][end] = 1
      
#정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
      
      