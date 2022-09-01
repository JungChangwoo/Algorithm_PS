# [부분 합]
# 1806번
import sys
n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

sums = [0] * (n+1)
value = 0
for i in range(1, n+1):
  value += data[i-1]
  sums[i] = value

INF = int(1e9)
result = INF
start = 1
end = 1
while True:
  if start > end:
    break
  # 부분합이 s 이상이라면
  if sums[end] - sums[start-1] >= s:
    result = min(result, end-start+1)
    start += 1
  # 부분합이 s 미만이라면
  else:
    end += 1
    # 마지막에 도달했다면
    if end == n+1:
      break

if result == INF:
  print(0)
else:
  print(result)
