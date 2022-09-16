# [회의실 배정]
# 1931번
import sys

n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: (x[1], x[0]))

start = data[0][1]
result = 1
for idx in range(1, len(data)):
    if data[idx][0] >= start:
        result += 1
        start = data[idx][1]

print(result)
