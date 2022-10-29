# [가장 긴 바이토닉 부분 수열]
# 11054번
import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

up = [1] * n
down = [1] * n

for i in range(n):
  for j in range(i):
    if array[j] < array[i]:
      up[i] = max(up[i], up[j] + 1)

for i in range(n-1, -1, -1):
  for j in range(n-1, i, -1):
    if array[i] > array[j]:
      down[i] = max(down[i], down[j] + 1)

result = 0
for i in range(n):
  value = up[i] + down[i]
  result = max(result, value)

print(result-1)
    