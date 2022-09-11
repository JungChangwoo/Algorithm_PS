data = [-2, -1, 0, 6]
from bisect import bisect_left

result = bisect_left(data[1:], 2)

print(result)
