# [두 배열의 합]
# 2143번
import sys
from bisect import bisect_left, bisect_right
T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
A = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
B = [0] + list(map(int, sys.stdin.readline().split()))

# 구간합 구하기
value = 0
for i in range(1, n+1):
  value += A[i]
  A[i] = value
value = 0
for i in range(1, m+1):
  value += B[i]
  B[i] = value

# 부 집합의 모든 경우의 수 구하기
A_sum = []
for i in range(n):
  for j in range(1, n+1):
    if j+i >= n+1:
      continue
    right = A[j+i]
    left = A[j-1]
    value = right - left
    A_sum.append(value)

B_sum = []
for i in range(m):
  for j in range(1, m+1):
    if j+i >= m+1:
      continue
    right = B[j+i]
    left = B[j-1]
    value = right - left
    B_sum.append(value)

B_sum.sort()

def count_by_value(a, left_value, right_value):
  left_index = bisect_left(a, left_value)
  right_index = bisect_right(a, right_value)
  return right_index - left_index

result = 0
for a_sum in A_sum:
  find_value = T - a_sum
  result += count_by_value(B_sum, find_value, find_value)
  
print(result)
    

