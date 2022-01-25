# 문제명 : 떡볶이 떡 만들기
# 문제 : 절단기에 높이를 지정하면 떡을 절단합니다. 높이보다 긴 떡은 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다. 손님은 잘리고 남은 위의 부분의 길이만큼 가져갑니다. 이때, 손님이 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 나의 답
from bisect import bisect_left
n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort() 

require = 0
for i in range(data[len(data)-1], 0, -1):
  range_index = bisect_left(data, i)
  for j in range(range_index, len(data)):
    require += data[j] - i
  if require >= m:
    break
  else:
    require = 0

print('result : ', i)

###########################################################
# 이코테 답
# 떡의 개수(n)와 요청한 떡의 길이(m)을 입력
n, m = map(int, input().split())
data = list(map(int, input().split()))
# 이때, 이진 탐색 문제는 입력 데이터의 개수가 많을 수 있다.
import sys
data = list(map(int, sys.stdin.readline().rstrip().split()))
# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(data)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
  total = 0
  mid = (start+end) // 2 
  for x in data:
    # 잘랐을 때의 양 계산
    if x > mid:
      total += x-mid
  # 조건을 충족하지 못했을 때 떡을 더 많이 자름 (왼쪽 탐색)
  if total < m:
    end = mid - 1
  # 조건을 충족했을 때 떡을 더 적게 자름 (오른쪽 탐색)
  else:
    start = mid + 1
    result = mid # 최대한 덜 잘랐을 때가 정답

print(result)

# 문제 해결 아이디어
# - 적절한 높이를 찾을 때까지 이진 탐색을 수행하며 높이 조정
# - "현재 이 높이로 자르면 조건을 만조할 수 있는가?"를 확인한 뒤에 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
# - 절단기의 높이는 0부터 10억까지의 정수 중 하나이다. 
# => 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 한다.
# 배운 점
# - 조건을 보고 큰 탐색 범위일 때 이진 탐색을 떠올릴 수 있어야 한다.
# - 이진 탐색을 할 때 중간점을 무엇으로 할 것인가