# [RGB 거리2]
# 17404번
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
  data.append(list(map(int, sys.stdin.readline().split())))
INF = int(1e9)

def get_color(color):
  if color == 0:
    return 1, 2
  if color == 1:
    return 0, 2
  if color == 2:
    return 0, 1
def rgb2(idx, color, scolor):
  # 만약 마지막에 도착했다면
  if idx == 0:
    if scolor == color:
      return INF
    else:
      return data[idx][color]
  # 이미 계산된 값이라면
  if d[idx][color] != INF:
    return d[idx][color]  
  # 갈 수 있는 color 구하기
  color1, color2 = get_color(color)
  result1 = rgb2(idx-1, color1, scolor) + data[idx][color]
  result2 = rgb2(idx-1, color2, scolor) + data[idx][color]
  d[idx][color] = min(d[idx][color], result1, result2)
  return d[idx][color]

result = INF
for i in range(3):
  d = [[INF, INF, INF] for _ in range(n)]
  rgb2(n-1, i, i)
  result = min(result, d[n-1][i])
print(result)
# 빨, 초 파
# d[i][빨] = min(d[i-1][초], d[i-1][파]) + d[i][빨]
# 단, 시작과 끝이 같은 경우에는 안 됨