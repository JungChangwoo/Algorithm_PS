# [LCS]
# 최장 공통 부분 수열

# [완전탐색버전]
# 시간복잡도 O(2^n)
# - X의 모든 부분 서열 중에서
# - Y의 부분 서열인 것들의 길이를 구한 뒤
# - 이 길이들 중에서 최대값을 찾는다.

# [재귀적으로 정의]
# 시간복잡도 O(2^n)
def lcs(x, y):
  m, n = len(x), len(y)
  if m == 0 or n == 0:
    return 0
  else:
    if x[-1] == y[-1]:
      return lcs(x[:(m-1)], y[:(n-1)]) + 1
    else:
      return max(lcs(x[:m], y[:(n-1)]),
                 lcs(x[:(m-1)], y[:n]))

# [상향식]
# 시간복잡도 O(N**2)
def lcs(x, y):
  x, y = [' '] + x, [' '] + y
  m, n = len(x), len(y)
  c = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(1, m):
    for j in range(1, n):
      if x[i] == y[j]:
        c[i][j] = c[i-1][j-1] + 1
      else:
        c[i][j] = max(c[i][j-1], c[i-1][j])
  return c

# [최적해 찾기]
def lcs2(x, y):
  x, y = [' '] + x, [' '] + y
  m, n = len(x), len(y)
  c = [[0 for _ in range(n)] for _ in range(m)]
  d = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(1, m):
    for j in range(1, n):
      if x[i] == y[j]:
        c[i][j] = c[i-1][j-1] + 1
        d[i][j] = 1
      else:
        c[i][j] = max(c[i][j-1], c[i-1][j])
        d[i][j] = 2 if (c[i][j-1] > c[i-1][j]) else 3
  return c, d

def get_lcs(i, j, d, x):
  if i == 0 or j == 0:
    return ""
  else:
    if d[i][j] == 1:
      return get_lcs(i-1, j-1, d, x) + x[i]
    elif d[i][j] == 2:
      return get_lcs(i, j-1, d, x)
    else:
      return get_lcs(i-1, j, d, x)

x = list(input())
y = list(input())
c, d = lcs2(x, y)
print(c[len(x)][len(y)])
print(get_lcs(len(x), len(y), d, [' '] + x))