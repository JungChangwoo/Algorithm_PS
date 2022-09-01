# [팩토리얼 0의 개수]
import math
import sys
n = int(sys.stdin.readline().rstrip())
value = math.factorial(n)
value = str(value)
result = 0
for i in range(len(value)-1, -1, -1):
  if value[i] != '0':
    break
  result += 1
print(result)