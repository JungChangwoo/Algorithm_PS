# [IOIOI]
# 5525번
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
array = list(sys.stdin.readline().rstrip())

dp = [0] * (m+2)
dx = ['I', 'O', 'I']
def is_possible(idx):
  for i in range(3):
    if array[idx + i] != dx[i]:
      return False
  return True

for i in range(len(array) - 2):
  if array[i] == 'I':
    if is_possible(i):
      dp[i+2] = dp[i] + 1

result = 0
for i in range(2, len(dp)):
  if dp[i] >= n:
    result += 1
print(result)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
array = list(sys.stdin.readline().rstrip())

idx, count, result = 0, 0, 0
while idx < m:
  if array[idx:idx+3] == ['I', 'O', 'I']:
    idx += 2
    count += 1
    if count == n:
      count -= 1
      result += 1
  else:
    count = 0
    idx += 1
print(result)