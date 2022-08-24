# [리모컨]
# 1107번

import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
broken = []
if m != 0:
  broken = list(map(int, sys.stdin.readline().rstrip().split()))
length = len(str(n))

def remote():
  global result
  for i in range(1000001):
    isBroken = False
    # 만약 부서진 버튼으로 만든 값이라면
    for data in list(map(int, str(i))):
      if data in broken:
        isBroken = True
    if not isBroken:
      result = min(result, abs(n - i) + len(str(i)))
      
result = int(1e9)
remote()
if abs(100 - n) < result:
  result = abs(100 - n)
print(result)
