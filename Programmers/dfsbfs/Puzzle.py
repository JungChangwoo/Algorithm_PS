# [퍼즐 조각 채우기]
from collections import deque
import copy
def rotate_2d(list_2d):
    n, m = len(list_2d), len(list_2d[0])
    new = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]   
    return new

def BFS(graph, x, y, n, flag):
    q = deque([(x, y)])
    graph[x][y] = 2
    block = []
    idx = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == flag:
                graph[nx][ny] = 2
                q.append((nx, ny))
                block.append((idx, d))
        idx += 1
    return block

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(game_board, table):
    n = len(game_board)
    blocks = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                block = BFS(game_board, i, j, n, 0)
                blocks.append(block)
    result = 0
    for d in range(4):
        table = rotate_2d(table)
        rotated_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if rotated_table[i][j] == 1:
                    puzzle = BFS(rotated_table, i, j, n, 1)
                    if puzzle in blocks:
                        table = copy.deepcopy(rotated_table)
                        result += len(puzzle) + 1
                        blocks.pop(blocks.index(puzzle))
                    else:
                        rotated_table = copy.deepcopy(table)
                    
    return result