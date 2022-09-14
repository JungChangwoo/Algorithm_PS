# [용액]
# 2467번
import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

min_value = 4000000000
result = []
for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        total = data[start] + data[end] + data[i]
        if abs(total) <= min_value:
            min_value = abs(total)
            result = [data[i], data[start], data[end]]
        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            result.sort()
            print(*result)
            sys.exit()

print(*result)
