# [피보나치 함수]
# 1003번

import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
  n = int(sys.stdin.readline().rstrip())
  d_zero = [0] * (n+1)
  d_one = [0] * (n+1)
  if n == 0:
    print(1, 0)
  elif n == 1:
    print(0, 1)
  else:
    d_zero[0], d_one[0] = 1, 0
    d_zero[1], d_one[1] = 0, 1
    for i in range(2, n+1):
      d_zero[i] = d_zero[i-2] + d_zero[i-1]
      d_one[i] = d_one[i-2] + d_one[i-1]
    print(d_zero[n], d_one[n])