# [부등호]
# 2529번
import sys
sys.setrecursionlimit(10**9)
k = int(sys.stdin.readline().rstrip())
signs = list(sys.stdin.readline().split())

def DFS(prev, idx):
  global max_value, min_value
  if idx == k:
    value = int(''.join(map(str, temp)))
    max_value = max(max_value, value)
    min_value = min(min_value, value)
    return

  for now in range(10):
    if not visited[now]:
      sign = signs[idx]
      if sign == '<':
        if prev < now:
          visited[now] = True
          temp[idx + 1] = now
          DFS(now, idx + 1)
          visited[now] = False
          temp[idx + 1] = -1
      else:
        if prev > now:
          visited[now] = True
          temp[idx + 1] = now
          DFS(now, idx + 1)
          visited[now] = False
          temp[idx + 1] = -1

visited = [False] * 10
temp = [-1] * (k+1)
max_value = 0
min_value = int(10 ** 10)
  
for i in range(10):
  visited[i] = True
  temp[0] = i
  DFS(i, 0)
  visited[i] = False
  temp[0] = -1
  
print(str(max_value).zfill(k+1))
print(str(min_value).zfill(k+1))

