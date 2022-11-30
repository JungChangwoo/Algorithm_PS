# [개미 전사] Session 2

n = int(input())
data = list(map(int, input().split()))

d = [0] * n
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + data[i])

print(d[n-1])
###################################################
d = [0] * n
d[0] = data[0]
d[1] = max(data[0], data[1])
def dynamic(x):
  if x == 0:
    return d[0]
  if x == 1:
    return data[1]
  if d[x] != 0:
    return d[x]
  d[x] = max(dynamic(x-1), dynamic(x-2) + data[x])
  return d[x]

dynamic(n-1)
print(d[n-1])