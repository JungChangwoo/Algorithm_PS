# [외판원 순회2]
# 10971번

def promising(i, w, trace):
  flag = True
  # 마지막에 도달했는데 시작점으로 돌아오지 않는다면
  if i == n-1 and w[trace[n-1]][trace[0]] == 0:
    flag = False
  # 인접하지 않는다면
  elif i > 0  and w[trace[i-1]][trace[i]] == 0:
    flag = False
  # 방문한 곳을 또 방문한다면
  else:
    j = 0
    while j < i and flag:
      if trace[i] == trace[j]:
        flag = False
      j += 1
  return flag

# level, 인접행렬, 경로
def hamiltonian(i, w, trace, total):
  global result
  # 현재 노드가 조건에 성립한다면 (인접 and not visited)
  if promising(i, w, trace):
    # 마지막에 도달했다면
    if i == n-1:
      total += w[trace[n-1]][trace[0]]
      result = min(result, total)
    else:
      # 가능한 다음 노드의 경우의 수를 모두 탐색      
      for j in range(1, n):
        trace[i+1] = j
        hamiltonian(i+1, w, trace, total + w[trace[i]][trace[i+1]])

import sys
n = int(sys.stdin.readline().rstrip())
w = []
for _ in range(n):
  w.append(list(map(int, sys.stdin.readline().split())))
trace = [-1] * (n+1)
trace[0] = 0 

INF = int(1e9)
result = INF
hamiltonian(0, w, trace, 0)
print(result)