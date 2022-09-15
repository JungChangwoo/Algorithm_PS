# [스도쿠]
# 2239번
import sys

graph = []
for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def check_col(x, y, value):
    for col in range(9):
        if graph[x][col] == value:
            return False
    return True


def check_row(x, y, value):
    for row in range(9):
        if graph[row][y] == value:
            return False
    return True


def check_block(x, y, value):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if graph[nx + i][ny + j] == value:
                return False
    return True


def DFS(idx):
    if idx == len(blank):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end='')
            print()
        exit(0)

    for i in range(1, 10):
        x, y = blank[idx][0], blank[idx][1]
        # 가로, 세로, 블록 Check
        if check_col(x, y, i) and check_row(x, y, i) and check_block(x, y, i):
            graph[x][y] = i
            DFS(idx + 1)
            graph[x][y] = 0


DFS(0)
