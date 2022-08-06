# [퇴사]
# 14501번
import sys
n = int(sys.stdin.readline().rstrip())
t = []
p = []
for i in range(n):
  time, price = map(int, sys.stdin.readline().rstrip().split())
  t.append(time)
  p.append(price)

d = [0] * n
for i in range(n-1, -1, -1):
  start = i + t[i]
  if start <= n:
    d[i] += p[i]
    max_value = d[i]
    for j in range(start, n):
      max_value = max(max_value, d[j] + d[i])
    d[i] = max_value

print(max(d))
      