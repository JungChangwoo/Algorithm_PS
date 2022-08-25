# [계단 오르기]
# 2579번
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
  data.append(int(sys.stdin.readline().rstrip()))
d = [0] * n

for i in range(n):
  if i == 0:
    d[i] = data[i]
    continue
  if i == 1:
    d[i] = data[i-1] + data[i]
    continue
  if i == 2:
    d[i] = max(data[i-2] + data[i], data[i-1] + data[i])
    continue
  
  d[i] = max(data[i-1] + d[i-3], d[i-2]) + data[i]

print(d[n-1])
