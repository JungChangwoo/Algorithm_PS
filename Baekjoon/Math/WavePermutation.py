# [파도반 수열]
# 9461번
import sys
d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2
d[5] = 3

for i in range(6, 101):
  d[i] = d[i-1] + d[i-5]

for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  print(d[n-1])