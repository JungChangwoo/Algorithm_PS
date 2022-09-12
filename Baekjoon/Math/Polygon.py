# [다각형의 면적]
# 2166번
import sys

n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.append(data[0])

left = 0
right = 0
for i in range(n):
    left += data[i][0] * data[i + 1][1]
    right += data[i][1] * data[i + 1][0]

result = round(abs(left - right) / 2, 1)
print(result)
