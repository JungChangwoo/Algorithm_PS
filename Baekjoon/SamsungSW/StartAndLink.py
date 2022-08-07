# [스타트와 링크]
# 14889번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

cases = []
for i in range(n):
  cases.append(i)
from itertools import combinations
cases = list(combinations(cases, n // 2))

result = int(1e9)
# 조합마다 양 팀의 격차를 구함
for case in cases:
  teamA = case
  teamB = []
  for i in range(n):
    if i not in case:
      teamB.append(i)
  # 각 팀의 능력치 구하기
  valueA = 0
  for i in teamA:
    for j in range(n):
      if j in teamA:
        valueA += graph[i][j]
  valueB = 0
  for i in teamB:
    for j in range(n):
      if j in teamB:
        valueB += graph[i][j]
  difference = abs(valueA - valueB)
  result = min(result, difference)

print(result)