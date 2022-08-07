# [톱니바퀴]
# 14891번

wheel = []
for i in range(4):
  wheel.append(list(map(int, input())))
k = int(input())
rotateOrder = []
for i in range(k):
  rotateOrder.append(list(map(int, input().split())))

def rotate(idx, d):
  global wheel
  now = idx
  visited[now] = True
  left = now - 1
  right = now + 1
  # 왼쪽 확인
  if 0 <= left < 4:
    if visited[left] == False and wheel[left][2] != wheel[now][6]:
      if d == 1:
        wheel[left][2]
        rotate(left, -1)
      else:
        rotate(left, 1)
  # 오른쪽 확인
  if 0 <= right < 4:
    if visited[right] == False and wheel[right][6] != wheel[now][2]:
      if d == 1:
        rotate(right, -1)
      else:
        rotate(right, 1)
  # 회전한다.
  if d == 1:
    a, b, c, d, e, f, g, h = wheel[idx]
    a, b, c, d, e, f, g, h = h, a, b, c, d, e, f, g
    wheel[idx] = a, b, c, d, e, f, g, h
  else:
    a, b, c, d, e, f, g, h = wheel[idx]
    a, b, c, d, e, f, g, h = b, c, d, e, f, g, h, a
    wheel[idx] = a, b, c, d, e, f, g, h
    

  
for order in rotateOrder:
  visited = [False] * 4
  idx, d = order
  rotate(idx-1, d)

result = 0
import math
for i in range(4):
  if wheel[i][0] == 1:
    result += int(math.pow(2, i))
print(result)
  