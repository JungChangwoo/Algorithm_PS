# [종이의 개수]
# 1780번
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

def get_count(x, y, length):
  global count_neg, count_zero, count_pos
  case = graph[x][y]
  for i in range(x, x + length):
    for j in range(y, y + length):
      if graph[i][j] != case:
        return False
  if case == -1:
    count_neg += 1
  elif case == 0:
    count_zero += 1
  else:
    count_pos += 1
  return True

def DFS(x, y, length):
  if length == 1:
    get_count(x, y, length)
    return
  is_possible = get_count(x, y, length)
  if is_possible:
    return
  length = length // 3
  DFS(x, y, length)
  DFS(x+length, y, length)
  DFS(x+length*2, y, length)
  DFS(x, y+length, length)
  DFS(x, y+length*2, length)
  DFS(x+length, y+length, length)
  DFS(x+length, y+length*2, length)
  DFS(x+length*2, y+length, length)
  DFS(x+length*2, y+length*2, length)

count_neg = 0
count_pos = 0
count_zero = 0
DFS(0, 0, n)
print(count_neg)
print(count_zero)
print(count_pos)