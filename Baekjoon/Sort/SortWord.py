# [단어 정렬]
# 문제 번호: 1181
import sys
n = int(input())
data = []
for i in range(n):
  data.append(sys.stdin.readline().rstrip())
  
data = list(set(data))
result = sorted(data, key = lambda x: (len(x), x))

for i in result:
  print(i)