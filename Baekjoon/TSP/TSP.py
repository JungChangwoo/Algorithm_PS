# [외판원 순회]
# 2098번
import sys

# 부분집합 포함 확인
def isIn(i, A):
  if A & (1 << (i-2)) != 0:
    return True
  else:
    return False

# 차집합 (비트를 0으로 만든다.)
def diff(A, j):
  t = 1 << (j-2)
  return A & (~t)

# A의 원소 갯수 확인
def count(A, n):
  count = 0
  for i in range(n):
    if A & (1 << i) != 0:
      count += 1
  return count

def minimun(W, D, i, A):
  minValue = INF
  minJ = 1
  n = len(W) - 1
  for j in range(2, n+1):
    if isIn(j, A):
      m = W[i][j] + D[j][diff(A, j)]
      if minValue > m:
        minValue = m
        minJ = j
  return minValue, minJ

# TSP
def travel(w):
  n = len(w) - 1
  size = 2 ** (n-1)
  D = [[0] * size for _ in range(n+1)]
  P = [[0] * size for _ in range(n+1)]
  # A가 공집합인 경우
  for i in range(2, n+1):
    D[i][0] = w[i][1]
  # A의 원소 갯수 
  for k in range(1, n-1):
    for A in range(1, size):
      # A의 갯수가 k인 경우
      if count(A, n) == k:
        for i in range(2, n+1):
          # i(출발노드)는 부분집합에 포함 X
          if not isIn(i, A):
            D[i][A], P[i][A] = minimun(W, D, i, A)
  A = size - 1
  D[1][A], P[1][A] = minimun(W, D, 1, A)
  return D, P

INF = int(1e9)
n = int(sys.stdin.readline().rstrip())
W = []
W.append([-1] * (n+1))
for _ in range(n):
  W.append([-1] + list(map(int, sys.stdin.readline().split())))
for i in range(1, n+1):
  for j in range(1, n+1):
    if i != j and W[i][j] == 0:
      W[i][j] = INF

D, P = travel(W)
print(D[1][2**(len(W)-2)-1])
      