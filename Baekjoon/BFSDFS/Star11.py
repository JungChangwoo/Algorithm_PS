# [별 찍기 - 11]
# 2448번
import sys
n = int(sys.stdin.readline().rstrip())
graph = [[' '] * (n*2) for _ in range(n)]

def recursion(x, y, size):
  if size == 3:
    graph[x][y] = '*'
    graph[x+1][y-1] = graph[x+1][y+1] = '*'
    for i in range(y-2, y+3):
      graph[x+2][i] = '*'
    return
  mid = size // 2
  recursion(x, y, mid)
  recursion(x + mid, y - mid, mid)
  recursion(x + mid, y + mid, mid)

recursion(0, n-1, n)
for i in graph:
  print("".join(i))