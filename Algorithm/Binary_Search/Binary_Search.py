# 이진 탐색 알고리즘
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 특징 : 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
# 시간 복잡도 : O(logN)을 보장함
##########################################################
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = start + end // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print('원소가 존재하지 않습니다.')
else:
  print(result+1)
##########################################################
# 이진 탐색 소스코드 구현 (반복문)
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))


# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print('원소가 존재하지 않습니다.')
else:
  print(result+1)