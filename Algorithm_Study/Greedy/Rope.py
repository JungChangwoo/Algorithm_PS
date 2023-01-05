# [로프]
# 2217번
import sys
n = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
array.sort()
result = -1
for i in range(len(array)):
  result = max(result, array[i] * (n-i))
print(result)
