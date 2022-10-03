# [용액]
# 2467번
import sys
from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

start = 0
end = n - 1
path = [0, 0]

INF = int(1e9)
min_value = INF
# 만약 음 or 양만 있다면
if data[start] >= 0 and data[end] > 0:
    path[0], path[1] = data[0], data[1]
elif data[start] < 0 and data[end] <= 0:
    path[0], path[1] = data[n - 2], data[n - 1]
# 음양이 모두 있다면
else:
    while data[start] < 0:
        # 1. 이분 탐색을 진행한다.
        idx = bisect_left(data, -data[start])
        if idx == n:
            idx -= 1
        # 2. 가장 0에 가까운 것을 선택 (bisect에서 나온 idx와 idx-1 비교)
        right = abs(data[start] + data[idx])
        left = INF
        # idx - 1이 start 가 아닐 경우에만
        if idx - 1 != start:
            left = abs(data[start] + data[idx - 1])
        value = min(left, right)
        if value < min_value:
            if left < right:
                path[0], path[1] = data[start], data[idx - 1]
            else:
                path[0], path[1] = data[start], data[idx]
            min_value = value
        start += 1

path.sort()
print(*path)
