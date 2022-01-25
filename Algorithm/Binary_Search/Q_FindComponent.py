# 문제명 : 부품찾기
# 문제 : 가게 N개의 부품이 있으며 각 부품은 고유 번호가 존재한다. 어느날 손님이 M개의 부품을 요청했다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하시오. (시간복잡도는 N log N 이여야 한다 )

# 이진 탐색
n = int(input())
shopArray = list(map(int, input().split()))

m = int(input())
custArray = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  return None

shopArray.sort()

for i in custArray:
  result = binary_search(shopArray, i, 0, n-1)
  if result == None:
    print('no', end = ' ')
  else:
    print('yes', end = ' ')

# 계수 정렬
n = int(input())
shopArray = list(map(int, input().split()))

m = int(input())
custArray = list(map(int, input().split()))

count_Array = [0] * (max(shopArray) + 1)
for i in shopArray:
  count_Array[i] += 1

for i in custArray:
  if count_Array[i] == 0:
    print('no', end = ' ')
  else:
    print('yes', end=' ')

# 집합 (특정 데이터가 존재하는지 검사할 때 매우 효과적임)
n = int(input())
shopArray = set(map(int, input().split()))
m = int(input())
custArray = list(map(int, input().split()))

for i in custArray:
  if i in shopArray:
    print('yes', end = ' ')
  else:
    print('no', end=' ')