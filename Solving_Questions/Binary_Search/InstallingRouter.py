# [공유기 설치]
# 도현이의 집 N개가 수직선 위에 있습니다. 집 여러 개가 같은 좌표를 가지는 일은 없습니다. 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 합니다. 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하려고 합니다.
# (2 <= N <= 200,000)
# (2 <= C <= N)
# 풀이 시간 : 50분
# 시간 제한 : 2초

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
  array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while(start <= end):
  mid = (start+end) // 2
  value = array[0]
  count = 1
  # 현재의 mid 값을 이용해 공유기 설치 
  for i in range(1, n): # 앞에서부터 차근차근 설치
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    start = mid + 1
    result = mid
  else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    end = mid - 1

print(result)

# [배운 점]
# - 제시되는 조건을 모두 확인해야 할 것 같은지
# --- 만약 그렇다면, 시간 제한을 보고 이진탐색을 떠올릴 수 있어야 한다
# - 이진 탐색을 쓸 것이라면, 정렬이 필요하다는 것!
# - 파라메트릭 서치 유형 ('떡볶이 떡 만들기')
