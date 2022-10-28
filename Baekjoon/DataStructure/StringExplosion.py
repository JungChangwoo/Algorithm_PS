# [문자열 폭발]
# 9935번
import sys
array = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
for i in range(len(array)):
  stack.append(array[i])
  if stack[-1] == bomb[-1]:
    if stack[-len(bomb):-1] == bomb[:-1]:
      for j in range(len(bomb)):
        stack.pop()

if len(stack) == 0:
  print('FRULA')
else:
  print("".join(stack))

