# 문제명 : 정렬된 배열에서 특정 수의 개수 구하기
# 문제 : N개의 원소를 가진 수열이 오름차순으로 정렬돼있다. 이때 이 수열에서 X가 등장하는 횟수를 계산하시오. 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계해야 한다.

# 나의 답
n, x = map(int, input().split())
array = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count_element(array, left, right):
  left_index = bisect_left(array, left)
  right_index = bisect_right(array, right)
  return right_index - left_index

result = count_element(array, x, x)

if result == 0:
  print(-1)
else:
  print(result)