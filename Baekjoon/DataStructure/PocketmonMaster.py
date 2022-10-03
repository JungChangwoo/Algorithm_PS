# [나는야 포켓몬 마스터 이다솜]
# 1620번
import sys
n, m = map(int, sys.stdin.readline().split())
key_dict = {}
value_dict = {}
for i in range(1, n+1):
  data = sys.stdin.readline().rstrip()
  key_dict[i] = data
  value_dict[data] = i

for i in range(m):
  value = sys.stdin.readline().rstrip()
  if value.isalpha():
    print(value_dict[value])
  else:
    print(key_dict[int(value)])
  