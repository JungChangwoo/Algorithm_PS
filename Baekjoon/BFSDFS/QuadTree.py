sq# [쿼드트리]
# 1992번
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().rstrip()))

def get_possible(x, y, length):
  case = graph[x][y]
  for i in range(x, x + length):
    for j in range(y, y + length):
      if graph[i][j] != case:
        return False
  return True

def DFS(x, y, length):
  if length == 1:
    return graph[x][y]
  is_possible = get_possible(x, y, length)
  if is_possible:
    return graph[x][y]
  word = '('
  length = int(length / 2)
  word += DFS(x, y, length)
  word += DFS(x, y + length, length)
  word += DFS(x + length, y, length)
  word += DFS(x + length, y + length, length)
  word += ')'
  return word

print(DFS(0, 0, n))