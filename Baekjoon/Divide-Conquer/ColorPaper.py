# [색종이]
# 2630번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

def isPossible(size, x, y):
  global white, blue
  color = graph[x][y]
  for i in range(x, x + size):
    for j in range(y, y + size):
      if graph[i][j] != color:
        return False
  if color == 0:
    white += 1
  else:
    blue += 1
  return True
    

def ColorPaper(size, x, y):
  possible = isPossible(size, x, y)
  if possible:
    return
  if size == 1:
    return
  size = size // 2
  ColorPaper(size, x, y)
  ColorPaper(size, x, y + size)
  ColorPaper(size, x + size, y)
  ColorPaper(size, x + size, y + size)

white = 0
blue = 0
ColorPaper(n, 0, 0)
print(white)
print(blue)