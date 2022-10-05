import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  d = [0] * (n+1)
  d[0] = 1
  for i in range(1, n+1):
    if i - 1 >= 0:
      d[i] += d[i-1]
    if i - 2 >= 0:
      d[i] += d[i-2]
    if i - 3 >= 0:
      d[i] += d[i-3]
  print(d[n])