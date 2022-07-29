# [바닥 공사]
n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3
def floorConstruction(x):
  if x == 1:
    return d[1]
  if x == 2:
    return d[2]
  for i in range(3, x+1):
    d[i] = (d[i-2] * 2 + d[i-1]) % 796796
  return d[x]

result = floorConstruction(n)
print(result)