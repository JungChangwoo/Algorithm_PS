# [부분수열의 합 2]
# 1208번

import sys
from bisect import bisect_left, bisect_right


def count_by_value(array, target):
    left_idx = bisect_left(array, target)
    right_idx = bisect_right(array, target)
    return right_idx - left_idx


# 시작, 끝, 합, 배열 (왼 or 오)
def BFS(start, end, sum, array):
    if start > end:
        array.append(sum)
        return
    BFS(start + 1, end, sum + data[start], array)
    BFS(start + 1, end, sum, array)


n, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

left = []
right = []
BFS(0, n // 2, 0, left)
BFS(n // 2 + 1, n - 1, 0, right)

right.sort()
result = 0
for i in range(len(left)):
    left_sum = left[i]
    target = S - left_sum
    count = count_by_value(right, target)
    result += count
if S == 0:
    result -= 1
print(result)
