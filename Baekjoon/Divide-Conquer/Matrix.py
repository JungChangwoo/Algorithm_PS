# [행렬 제곱]
# 10830번
import sys
n, b = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
  a.append(list(map(int, sys.stdin.readline().split())))

def square(a, b):
  if b == 1:
    for i in range(n):
      for j in range(n):
        a[i][j] %= 1000
    return a
  temp = square(a, b // 2)
  if b % 2:
    return mul(mul(temp, temp), a)
  else:
    return mul(temp, temp)

def mul(a, b):
  z = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      value = 0
      for k in range(n):
        value += a[i][k] * b[k][j]
      z[i][j] = value % 1000
  return z

result = square(a, b)
for i in range(n):
  print(*result[i])