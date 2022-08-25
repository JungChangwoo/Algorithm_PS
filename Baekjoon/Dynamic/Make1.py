# [1로 만들기]
# 1463번

import sys
n = int(sys.stdin.readline().rstrip())
INF = int(1e9)
d = [INF] * (n+1)

d[1] = 0
for i in range(1, n+1):
  # 만약 -1이 가능하다면
  if i - 1 >= 1:
    d[i] = min(d[i], d[i-1] + 1)
  # 만약 3으로 나누어 떨어진다면
  if i % 3 == 0:
    d[i] = min(d[i], d[int(i / 3)] + 1)
  # 만약 2로 나누어 떨어진다면
  if i % 2 == 0:
    d[i] = min(d[i], d[int(i / 2)] + 1)

print(d[n])