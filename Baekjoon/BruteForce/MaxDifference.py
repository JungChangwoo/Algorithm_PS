# [차이를 최대로]
# 10819번
import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

visited = [False] * n
temp = [0] * n

def get_value():
  total = 0
  for i in range(n-1):
    total += abs(temp[i] - temp[i+1])
  return total
  
def DFS(idx):
  global result
  if idx == n:
    result = max(result, get_value())
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      temp[idx] = array[i]
      DFS(idx + 1)
      visited[i] = False
      temp[idx] = 0

result = 0
DFS(0)
print(result)
  