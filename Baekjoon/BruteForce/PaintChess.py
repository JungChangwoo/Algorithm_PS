# [체스판 다시 칠하기]
# 1018번
import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().rstrip()))

def check(x, y):
  case1 = ['W', 'B']
  case2 = ['B', 'W']
  count1 = 0
  count2 = 0
  for i in range(x, x + 8):
    for j in range(y, y + 8):
      if case1[(i + j) % 2] != graph[i][j]:
        count1 += 1
      if case2[(i + j) % 2] != graph[i][j]:
        count2 += 1
  return min(count1, count2)
    
result = int(1e9)
for i in range(n - 7):
  for j in range(m - 7):
    result = min(result, (check(i, j)))
print(result)


    