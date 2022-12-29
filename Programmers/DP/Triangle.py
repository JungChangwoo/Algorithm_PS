# [정수삼각형]
def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for x in range(1, n):
        for y in range(len(triangle[x])):
            if y == 0:
                dp[x][y] = dp[x-1][y] + triangle[x][y]
            if y == len(triangle[x]) - 1:
                dp[x][y] = dp[x-1][y-1] + triangle[x][y]
            else:
                dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + triangle[x][y]
    return max(dp[n-1])