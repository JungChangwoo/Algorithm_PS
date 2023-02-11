# [블록 이동하기]
from collections import deque

def get_moves(cur1, cur2):
    global new_board
    moves = []
    # 수평이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for d in range(4):
        nxt1 = (cur1[0] + dx[d], cur1[1] + dy[d])
        nxt2 = (cur2[0] + dx[d], cur2[1] + dy[d])
        if new_board[nxt1[0]][nxt1[1]] == 0 and new_board[nxt2[0]][nxt2[1]] == 0:
            moves.append((nxt1, nxt2))
    # 세로
    if cur1[1] == cur2[1]:
        for d in [-1, 1]:
            if new_board[cur1[0]][cur1[1] + d] == 0 and new_board[cur2[0]][cur2[1] + d] == 0:
                moves.append(((cur1[0], cur1[1] + d), cur1))
                moves.append(((cur2[0], cur2[1] + d), cur2))
    # 가로
    else:
         for d in [-1, 1]:
            if new_board[cur1[0] + d][cur1[1]] == 0 and new_board[cur2[0] + d][cur2[1]] == 0:
                moves.append((cur1, (cur1[0] + d, cur1[1])))
                moves.append((cur2, (cur2[0] + d, cur2[1])))
    return moves

def bfs(cur1, cur2):
    global n, new_board
    q = deque([(cur1, cur2, 0)])
    visited = set([(cur1, cur2)])
    
    while q:
        cur1, cur2, count = q.popleft()

        if cur1 == (n, n) or cur2 == (n, n):
            return count
        
        for move in get_moves(cur1, cur2):
            if move not in visited:
                visited.add(move)
                q.append((move[0], move[1], count + 1))

def solution(board):
    global n, new_board
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    result = bfs((1, 1), (1, 2))
    return result