# [이진 검색 트리]
# 5639번
import sys
sys.setrecursionlimit(10**9)
array = []
while True:
  try:
    data = int(sys.stdin.readline().rstrip())
    array.append(data)
  except:
    break

def DFS(start, end):
  if start > end:
    return
  mid = end + 1
  for i in range(start + 1, end + 1):
    if array[start] < array[i]:
      mid = i
      break
  DFS(start + 1, mid - 1)
  DFS(mid, end)
  print(array[start])

DFS(0, len(array) - 1)