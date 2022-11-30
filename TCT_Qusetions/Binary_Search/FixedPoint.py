# [고정점 찾기]
# 오름차순의 하나의 수열에서 그 값이 인덱스와 동일한 원소를 찾으시오. 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

n = int(input())
data = list(map(int, input().split()))

def binary_search(array, start, end):
  if start > end:
    return -1
  mid = (start + end) // 2
  if array[mid] == mid:
    return mid
  elif array[mid] > mid:
    return binary_search(array, start, mid-1)
  else:
    return binary_search(array, mid+1, end)

print(binary_search(data, 0, len(data)-1))


  