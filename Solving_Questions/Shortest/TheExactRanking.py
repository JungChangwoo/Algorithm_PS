# [정확한 순위]
# 선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있습니다. 학생 N명의 성적은 모두 다릅니다. 학생들의 성적을 비교한 결과가 주어질 째, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하세요.

# 나의 답
n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  data[a].append(b)

result = 0
student = 0

# 진입 간선 따라가기
from collections import deque
def in_check(visited, start):
  global result
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    for i in range(1, n+1):
      if visited[i] == True:
        continue
      for j in range(len(data[i])):
        if data[i][j] == v:
          q.append(i)
          visited[i] = True
          result += 1
          print('input : ', i, 'result : ', result)

# 진출 간선 따라가기
def out_check(visited, start):
  global result
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    for i in data[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        result += 1
        print('output : ', i, 'result : ', result)

# 각 노드 반복
for i in range(1, n+1):
  print('now : ', i)
  visited = [False for _ in range(n+1)]
  # 진입 간선 따라가기
  in_check(visited, i)
  # 진출 간선 따라가기
  out_check(visited, i)
  # 전체 노드를 거치는지
  if result == n-1:
    student += 1
  # 초기화
  result = 0

print(student)

# 이코테 답
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for a in range(1, n+1):
      graph[a][b] = graph[a][k] + graph[k][b]

result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    result += 1

print(result)

# 문제 풀이 아이디어
# - A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적 비교'가 가능하다는 것이다.
# - 모든 노드에 대하여 다른 노드와 서로 도달이 가능한지를 체크하여 문제 해결