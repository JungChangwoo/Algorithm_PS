# [숨바꼭질]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 1초
# 메모리 제한: 128MB

import heapq

n, m = map(int, input().split())

INT = int(1e9)
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

distance = [INT] * (n+1)
start = 1

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))

dijkstra(start)

max = 0
for i in distance:
  if i != INT:
    if i > max:
      max = i

count = 0
num = 0
for i in range(len(distance)):
  if distance[i] == max:
    if count == 0:
      num = i
    count += 1

print(distance)
print(num, max, count)
  