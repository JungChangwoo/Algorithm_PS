# [공유기 설치]
# 풀이 시간 : 50분
# 시간 제한 : 2초
import sys
n, c = list(map(int, input().split(' ')))
array = []
for i in range(n):
  array.append(int(sys.stdin.readline().rstrip()))

array.sort()

start = 1
end = (array[n-1] - array[0])
result = 0

while start <= end:
  mid = (start + end) // 2
  # 되는지 안 되는지 확인
  value = array[0]
  count = 1
  for i in range(1, n):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  # 가능 =>  더 큰 값으로 or 불가능 => 더 작은 값 
  if count >= c:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)

# [배운 점]                                                                                 
# - 제시되는 조건을 모두 확인해야 할 것 같은지
# --- 만약 그렇다면, 시간 제한을 보고 이진탐색을 떠올릴 수 있어야 한다
# - 이진 탐색을 쓸 것이라면, 정렬이 필요하다는 것!
# - 파라메트릭 서치 유형 ('떡볶이 떡 만들기')
