# [듣보잡]
# 1764번
import sys
n, m = map(int, sys.stdin.readline().split())
unHear = {}
for i in range(n):
  data = sys.stdin.readline().rstrip()
  unHear[data] = i

result = []
for i in range(m):
  data = sys.stdin.readline().rstrip()
  if data in unHear:
    result.append(data)

print(len(result))
result.sort()
for i in result:
  print(i)