# [AC]
# 5430번

import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  func = list(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  array = input()[1:-1].split(',')
  # deque에 넣어줌
  deq = deque(array)

  isReverse = False
  left = 0
  right = 0
  # 함수를 하나씩 확인한다.
  for i in func:
    # 만약 R이 나왔다면
    if i == 'R':
      isReverse = not isReverse
    # 만약, D가 나왔다면
    if i == 'D':
      # 거꾸로 된 상태라면:
      if isReverse:
        right += 1
      else:
        left += 1

  # 만약, 없애는 함수가 배열의 길이보다 길다면
  if left+right > n:
    print('error')
    continue
  
  for _ in range(right):
    deq.pop()
  for _ in range(left):
    deq.popleft()
  
  # 만약, 거꾸로 상태라면
  if isReverse:
    deq.reverse()
    
  print("[" + ",".join(deq) + "]")