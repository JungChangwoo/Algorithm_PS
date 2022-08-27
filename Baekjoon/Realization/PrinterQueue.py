# [프린터 큐]
# 1966번

import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  q = deque()
  n, m = map(int, sys.stdin.readline().rstrip().split())
  array = list(map(int, sys.stdin.readline().rstrip().split()))
  
  for i in range(len(array)):
    if i == m:
      q.append((True, array[i]))
    else:
      q.append((False, array[i]))
      
  result = 0
  while q:
    flag, now = q.popleft()
    success = True
     # 만약, 자신보다 중요도가 높은 값이 있다면 뒤로
    for i in q:
      if now < i[1]:
        success = False
    if success:
      result += 1
      # 만약, 순서가 궁금한 값이였다면 return
      if flag == True:
        print(result)
        break
    else:
      q.append((flag, now))