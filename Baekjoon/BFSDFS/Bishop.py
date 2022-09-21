# [비숍]
# 1799번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

white = []
black = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
        black.append((i, j))
      else:
        white.append((i, j))

def DFS(bishop, idx, count):
  global resultB, resultW
  if idx == len(bishop):
    x, y = bishop[idx-1]
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
      resultB = max(resultB, count)
    else:
      resultW = max(resultW, count)
    return
  x, y = bishop[idx]
  if stripe_01[x+y] == True or stripe_02[x-y+n-1] == True:
    DFS(bishop, idx+1, count)
  else:
    stripe_01[x+y] = True
    stripe_02[x-y+n-1] = True
    DFS(bishop, idx+1, count + 1)
    stripe_01[x+y] = False
    stripe_02[x-y+n-1] = False
    DFS(bishop, idx+1, count)
    
resultW = 0
resultB = 0
stripe_01 = [False] * (n*2-1)
stripe_02 = [False] * (n*2-1)
if len(white) > 0:
  DFS(white, 0, 0)
if len(black) > 0:
  DFS(black, 0, 0)
print(resultW + resultB)
