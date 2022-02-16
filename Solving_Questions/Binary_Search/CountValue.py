# [정렬된 배열에서 특정 수의 개수 구하기]
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요. 단, 이 문제는 시간복잡도 O(log N)의 알고리즘을 설계해야 합니다.

# 라이브러리 사용
n, x = map(int, input().split())
data = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def countValue(array, left, right):
  left_index = bisect_left(array, left)
  right_index = bisect_right(array, right)
  return right_index - left_index

result = countValue(data, x, x)
if result == 0:
  print(-1)
else:
  print(result)
