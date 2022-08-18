# [LCS]
# 9251번
import sys
arrayA = list(sys.stdin.readline().rstrip())
arrayB = list(sys.stdin.readline().rstrip())
lenA = len(arrayA)
lenB = len(arrayB)

dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]

for i in range(1, lenA + 1):
  for j in range(1, lenB + 1):
    if arrayA[i-1] == arrayB[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
print(dp[lenA][lenB])

# 규칙이 머릿 속에서 잘 떠오르지 않는다면 경우를 따져보며 규칙을 얻어내자.