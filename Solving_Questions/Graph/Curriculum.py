# [커리큘럼]
# 난이도: 최상
# 권장 풀이 시간: 50분
# 시간 제한: 2초

n = int(input())
graph = [[] for _ in range(n + 1)]
value_array = [0 for _ in range(n + 1)]
in_array = [0 for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    data.remove(-1)
    value_array[i] = data[0]
    for j in range(1, len(data)):
        graph[data[j]].append(i)
        in_array[i] += 1

# 처음에 들어오는 간선이 없는 노드 찾음
from collections import deque

q = deque()
for i in range(1, n + 1):
    if in_array[i] == 0:
        q.append(i)
distance[1] = value_array[1]

while q:
    now = q.popleft()
    for i in graph[now]:
        cost = distance[now] + value_array[i]
        distance[i] = cost
        in_array[i] -= 1
        if in_array[i] == 0:
            q.append(i)

for i in range(1, n+1):
  print(distance[i])
