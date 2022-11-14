# [스택 수열]
# 1874번
import sys
n = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for i in range(n)]

stack = []
result = []
idx = 0
now = 0
while idx < n:
  if not stack:
    now += 1
    stack.append(now)
    result.append('+')
    continue
  if stack[-1] < array[idx]:
    now += 1
    stack.append(now)
    result.append('+')
  elif stack[-1] == array[idx]:
    value = stack.pop()
    result.append('-')
    idx += 1
  else:
    print('NO')
    sys.exit()
for i in result:
  print(i)

import sys
n = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for i in range(n)]

stack = []
result = []
idx = 0
for i in range(1, n+1):
  stack.append(i)
  result.append('+')
  while True:
    if not stack:
      break
    if stack[-1] == array[idx]:
      stack.pop()
      result.append('-')
      idx += 1
    elif stack[-1] > array[idx]:
      print('NO')
      sys.exit()
    else:
      break
  
for i in result:
  print(i)