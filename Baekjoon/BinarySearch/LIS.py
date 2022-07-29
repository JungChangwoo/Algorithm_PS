# 가장 긴 증가하는 부분 수열
# 문제 번호: 12015
import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

d = [1] * n
    
for i in range(1, n):
  for j in range(0, i):
    if data[j] < data[i]:
      d[i] = max(d[i], d[j] + 1)

print(max(d))
