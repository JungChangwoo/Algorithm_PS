# [정수 삼각형]
# 크기가 n인 정수 삼각형이 있다. 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하시오.
# (1 <= n <= 500)

n = int(input())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

d = []
for i in range(n):
  d.append([0 for _ in range(len(data[i]))])


def triangle(arrays, i, j):
  if i == n-1:
    return arrays[i][j]
  if d[i][j] != 0:
    return d[i][j]
  d[i][j] = max(triangle(arrays, i+1, j), triangle(arrays, i+1, j+1)) + arrays[i][j]
  return d[i][j]

print(triangle(data, 0, 0)) 