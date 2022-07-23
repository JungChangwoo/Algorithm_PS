# [편집 거리]
# 난이도: 중
# 권장 풀이 시간: 30분
# 시간 제한: 2초

arrayA = list(input())
arrayB = list(input())
n = len(arrayA)
m = len(arrayB)

INF = int(1e9)

dp = [[INF] * (m + 1) for _ in range(n + 1)]

# 공집합 초기화
for i in range(m + 1):
  dp[0][i] = i
for i in range(n + 1):
  dp[i][0] = i

for i in range(n):
  for j in range(m):
    # 같은 값인지 확인
    if arrayA[i] == arrayB[j]:
      dp[i+1][j+1] = dp[i][j]
    else:
      dp[i+1][j+1] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i][j])

print(dp[n][m])
