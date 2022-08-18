# [구간 합 구하기 5]
# 11660번
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
sections = []
for _ in range(m):
    sections.append(list(map(int, sys.stdin.readline().split())))

# (0,0) 으로부터의 구간합 구하기
for i in range(n):
    for j in range(n):
        leftX, leftY = i, j - 1
        upX, upY = i - 1, j
        if 0 <= leftX < n and 0 <= leftY < n:
            graph[i][j] += graph[leftX][leftY]
        if 0 <= upX < n and 0 <= upY < n:
            graph[i][j] += graph[upX][upY]
        if 0 <= i - 1 < n and 0 <= j - 1 < n:
            graph[i][j] -= graph[i - 1][j - 1]

result = []
# 명령에 맞는 구간합 구하기
for section in sections:
    startX, startY, endX, endY = section[0] - 1, section[1] - 1, section[
        2] - 1, section[3] - 1
    sum = graph[endX][endY]
    if 0 <= startY - 1 < n:
        sum -= graph[endX][startY - 1]
    if 0 <= startX - 1 < n:
        sum -= graph[startX - 1][endY]
    if 0 <= startX - 1 < n and 0 <= startY - 1 < n:
        sum += graph[startX - 1][startY - 1]
    result.append(sum)

for i in result:
    print(i)
