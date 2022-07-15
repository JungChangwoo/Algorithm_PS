# [최종 순위]
# 난이도: 상
# 권장 풀이 시간: 60분
# 시간 제한: 1초
# 메모리 제한: 128MB

from collections import deque

test = int(input())
for i in range(test):
  n = int(input())
  t = list(map(int, input().split()))

  cycle = False
  certain = True
  graph = [[False for _ in range(n+1)] for _ in range(n+1)]
  indegree = [0] * (n+1)

  for i in range(n):
    for j in range(i+1, n):
      graph[t[i]][t[j]] = True
      indegree[t[j]] += 1
  
  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    if graph[a][b]:
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1
      indegree[b] -= 1
    else:
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1

  result = []
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  
  for i in range(n):
    
    if len(q) == 0:
      cycle = True 
      break
      
    if len(q) >= 2:
      certain = False
      break
      
    now = q.popleft()
    result.append(now)
    for j in range(1, n+1):
      if graph[now][j] == True:
        indegree[j] -= 1
        if indegree[j] == 0:
          q.append(j)

  if cycle:
    print('IMPOSSIBLE')
  elif certain == False:
    print('?')
  else:
    for i in range(n):
      print(result[i], end=' ')
    print()
      