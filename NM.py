import sys
def dfs(arr, n, m):
  if len(arr) == m:
    result.append(arr[:])
    return
    
  for i in range(1, n+1):
    if not visited[i]:
      arr.append(i)
      visited[i] = True
      dfs(arr, n, m)
      visited[i] = False
      arr.pop()

n, m = map(int, sys.stdin.readline().split())
result = []
visited = [False] * (n+1)

dfs([], n, m)
for arr in result:
  print(*arr)