# [집합]
# 11723번
import sys
m = int(sys.stdin.readline().rstrip())

s = set()
for _ in range(m):
  data = sys.stdin.readline().rstrip().split()
  if len(data) == 1:
    if data[0] == 'all':
      s = set([str(i) for i in range(1, 21)])
    else:
      s = set()
  else: 
    compute, value = data[0], data[1]
    value = int(value)
    if compute == 'add':
      s.add(value)
    elif compute == 'check':
      print(1 if value in s else 0)
    elif compute == 'remove':
      s.discard(value)
    elif compute == 'toggle':
      if value in s:
        s.discard(value)
      else:
        s.add(value)


    
