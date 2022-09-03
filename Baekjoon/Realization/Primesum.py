# [소수의 연속합]
# 1644번
import sys
import math
n = int(sys.stdin.readline().rstrip())

array = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True: 
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

data = []
for i in range(2, n+1):
  if array[i]:
    data.append(i)

prefixsum = [0] * (len(data) + 1)
value = 0
for i in range(len(data)):
  value += data[i]
  prefixsum[i+1] = value

start = 1
end = 1
result = 0
while end < len(prefixsum):
  sum = prefixsum[end] - prefixsum[start-1]
  # 만약, 연속합이 값과 같다면
  if sum == n:
    result += 1
    end += 1
  # 만약, 연속합이 값보다 작다면
  elif sum < n:
    end += 1
  # 만약, 연속합이 값보다 크다면
  else:
    start += 1
  
print(result)