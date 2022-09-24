# [전깃줄 - 2]
# 2568번
import sys
from bisect import bisect_left
n = int(sys.stdin.readline().rstrip())
a = []
for _ in range(n):
  start, end = map(int, sys.stdin.readline().split())
  a.append((start, end))

a.sort()
d = [a[0][1]]
q = [-1] * n
for i in range(n):
  if d[-1] < a[i][1]:
    d.append(a[i][1])
    q[i] = max(q) + 1
  else:
    idx = bisect_left(d, a[i][1])
    d[idx] = a[i][1]
    q[i] = idx + 1

print(n - len(d))

lis = []
find_value = len(d)
for i in range(n-1, -1, -1):
  if find_value == 0:
    break
  if find_value == q[i]:
    lis.append(a[i])
    find_value -= 1
    
result = []
for i in a:
  if i not in lis:
    result.append(i)

result.sort(key = lambda x:x[0])
for i in result:
  print(i[0])
  

# [문제해결 아이디어]
# 시작의 인덱스가 증가하면서 끝의 선택지가 점점 줄어들지만 고른 값들이 모두 증가하는 방향
# => 도착점을 확인하면서 가장 긴 증가하는 부분수열을 하되, 어떤 집합인지를 알기 위해서 Q라는 길이를 저장하는 배열을 추가로 활용

# A = 문제에서 주어진 배열
# D = i+1 번째 길이 중 가장 작은 값을 저장하는 배열
# Q = i번째 idx에서 만들 수 있는 LIS의 길이를 저장하는 배열
