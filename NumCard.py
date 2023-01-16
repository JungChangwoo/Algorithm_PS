import sys
from collections import deque
for _ in range(int(sys.stdin.readline().rstrip())):
  opers = sys.stdin.readline().rstrip()
  n = int(sys.stdin.readline().rstrip())
  array = sys.stdin.readline().rstrip()[1:-1].split(',')
  if n == 0:
    array = []
  q = deque(array)

  isR = False
  isError = False
  for oper in opers:
    if oper == 'R':
      isR = not isR
    else:
      if not q:
        print('error')
        break
      elif isR:
        q.pop()
      else:
        q.popleft()
  else:
    if isR:
      q.reverse()
    print("[" + ",".join(q) + "]")