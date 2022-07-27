# [나무 자르기]
# 문제번호: 2805


# 절단기 높이 (0, 가장 높은 나무의 길이)
# 절단기 높이를 이진탐색으로 구할 수 있는 나무의 길이 계산
# 설정할 수 있는 높이의 최댓값

n, m = map(int, input().split())
array = list(map(int, input().split()))
end = max(array)

result = 0
def binary_search(array, target, start, end):
  global result
  if start > end:
    return -1
  mid = (start + end) // 2
  # 구할 수 있는 나무의 길이 최댓값 계산
  length = 0
  for i in array:
    value = i - mid
    if value > 0:
      length += value
  if length >= target:
    result = max(result, mid)
    return binary_search(array, target, mid + 1, end)
  elif length < target:
    return binary_search(array, target, start, mid - 1)


binary_search(array, m, 0, end)
print(result)

print("/////////////////////")
start = 0
end = end
target = m
result = 0
while start <= end:
  mid = (start + end) // 2
  length = 0
  for i in array:
    if i > mid:
      length += i - mid
  if length >= target:
    start = mid + 1
    result = max(result, mid)
  else:
    end = mid - 1
print(result)
