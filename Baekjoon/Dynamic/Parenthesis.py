# [괄호]
# 10422번
import sys
d = [0] * 5001
d[0] = 1

for i in range(2, 5001, 2):
  for j in range(2, i+1, 2):
    d[i] += d[j-2] * d[i-j]
  d[i] %= 1000000007

for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  print(d[n])
