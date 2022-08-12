# [거짓말]
# 1043번
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
truth = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, truth[0]):
  a = truth[i]
  b = truth[i + 1]
  graph[a].append(b)
  graph[b].append(a)

truth.pop(0)

party = []
for _ in range(m):
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  party.append(data)
  for i in range(1, data[0]):
    a = data[i]
    b = data[i + 1]
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def BFS(start):
  visited = [False] * (n + 1)
  q = deque([start])
  visited[start]
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        if i in truth:
          return False
        q.append(i)
        visited[i] = True
  return True

result = 0
# 파티를 돌면서 진실을 아는 사람과 연결된 사람이 있는지 확인
for i in range(m):
  data = party[i]
  isLier = False
  for j in range(1, data[0] + 1):
    if BFS(data[j]) == False:
      isLier = True
  if isLier == False:
    result += 1

print(result)