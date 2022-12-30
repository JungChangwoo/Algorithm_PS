# [등굣길]
def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    puddles = [[y, x] for [x, y] in puddles]
    dp[1][1] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y ==1: continue
            if [x, y] in puddles:
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x-1][y] + dp[x][y-1]) % 1000000007
    return dp[n][m]

def DFS(x, y, n, m, dp, puddles):
    if x == 0 or y == 0:
        return 0
    if x == 1 and y == 1:
        return 1
    if dp[x][y] == -1:
        return 0
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = (DFS(x, y-1, n, m, dp, puddles) + DFS(x-1, y, n, m, dp, puddles)) % 1000000007
    return dp[x][y]

def solution2(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for y, x in puddles:
        dp[x][y] = -1
    DFS(n, m, n, m, dp, puddles)
    return dp[n][m]