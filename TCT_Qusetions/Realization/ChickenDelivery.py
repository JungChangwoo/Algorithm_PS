# [치킨 배달]
# 난이도: 중상
# 권장 풀이 시간: 40분
# 시간 제한: 1초
import sys
n, m = map(int, input().split())
graph = []
for i in range(n):
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  graph.append(data)

INF = int(1e9)
# 모든 치킨집과 집의 위치 구하기
chicken = []
houses = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chicken.append((i, j))
    elif graph[i][j] == 1:
      houses.append((i, j))

def get_distance(chicken_com):
  result = 0
  for house in houses:
    min_distance = INF
    for chicken in chicken_com:
      distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
      min_distance = min(min_distance, distance)
    result += min_distance
  return result
  
from itertools import combinations
result = INF
def Chicken_Delivery():
  global result
  # 가능한 치킨집 조합을 반복 확인
  chicken_coms = list(combinations(chicken, m))
  for chicken_com in chicken_coms:
    # 도시 치킨 거리 최솟값 구하기
    distance = get_distance(chicken_com)
    result = min(result, distance)

Chicken_Delivery()
print(result)
# 도시의 치킨 거리 최솟값 구하기
# 1. 집은 모든 치킨집과의 거리 중 최솟값을 가짐
# 2. 1을 반복하면서 도시의 치킨 거리를 구함
