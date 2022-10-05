# [2xn 타일링]
# 11726번

# 각 열마다 채울 수 있는 경우의 수
# d[i] = d[i-1] + d[i-2]
# d[0] = 1
# d[1] = 1
# d[2] = 1 + 1
# d[3] = 1 + 2

import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * n
d[0] = 1
if n >= 2:
  d[1] = 2
for i in range(2, n):
  idx1 = i - 1
  idx2 = i - 2
  d[i] = d[idx1] + d[idx2]

print(d[n-1] % 10007)
