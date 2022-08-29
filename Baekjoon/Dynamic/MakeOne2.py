# [1로 만들기 2]
# 12852번
import sys
n = int(sys.stdin.readline().rstrip())
INF = int(1e9)
d = [INF] * (n+1)

d[1] = 0
for i in range(2, n+1):
  if i % 3 == 0 and i / 3 >= 1:
    d[i] = min(d[i], d[int(i / 3)] + 1)
  if i % 2 == 0 and i / 2 >= 1:
    d[i] = min(d[i], d[int(i / 2)] + 1)
  if i - 1 >= 1:
    d[i] = min(d[i], d[i - 1] + 1)

print(d[n])
idx = n
while True:
  if idx == 1:
    print(idx, end=' ')
    break
  print(idx, end=' ')
  min = INF
  minIdx = 0
  if idx % 3 == 0 and i / 3 >= 1:
    if d[int(idx / 3)] < min:
      min = d[int(idx / 3)]
      minIdx = int(idx / 3)
  if idx % 2 == 0 and i / 2 >= 1:
    if d[int(idx / 2)] < min:
      min = d[int(idx / 2)]
      minIdx = int(idx / 2)
  if idx - 1 >= 1:
    if d[idx - 1] < min:
      min = d[idx - 1]
      minIdx = idx - 1
  idx = minIdx
    
    