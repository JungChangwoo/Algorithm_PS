# [숫자 카드 2]
import sys

n = int(sys.stdin.readline().rstrip())
arrayA = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arrayB = list(map(int, sys.stdin.readline().rstrip().split()))

arrayA.sort()
print(arrayA)

from bisect import bisect_left, bisect_right


def count_by_value(array, left, right):
    left_index = bisect_left(array, left)
    right_index = bisect_right(array, right)
    return right_index - left_index


result = ''
for i in arrayB:
    count = count_by_value(arrayA, i, i)
    result += str(count) + ' '
print(result)

import sys

n = int(sys.stdin.readline().rstrip())
arrayA = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arrayB = list(map(int, sys.stdin.readline().rstrip().split()))

from collections import Counter

c = Counter(arrayA)

result = ''
for i in arrayB:
    if i in c:
        result += str(c[i]) + ' '
    else:
        result += '0 '
print(result)
