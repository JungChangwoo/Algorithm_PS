# [Dance Dance Revolution]
# 2342번
import sys
 
def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b-a)%2 == 0:
        return 4
    else:
        return 3

array = list(map(int, sys.stdin.readline().split()))
INF = int(1e9)
d = [[[INF] * 5 for _ in range(5)] for _ in range(len(array))]
d[0][0][0] = 0

for idx in range(1, len(array)):
  next = array[idx-1]
  for l in range(5):
    for r in range(5):
      d[idx][next][r] = min(d[idx][next][r], d[idx-1][l][r] + move(l, next))
      d[idx][l][next] = min(d[idx][l][next], d[idx-1][l][r] + move(r, next))

result = INF
for i in range(5):
  for j in range(5):
    result = min(result, d[len(array) - 1][i][j])
print(result)