# 가장 긴 증가하는 부분 수열 2
# 12015번
import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

lis = [data[0]]

def binary_search(lis, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if lis[mid] == target:
      return mid
    if target > lis[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return start 
  
for now in data:
  if lis[-1] < now:
    lis.append(now)
  else:
    idx = binary_search(lis, now, 0, len(lis)-1)
    lis[idx] = now

print(len(lis))