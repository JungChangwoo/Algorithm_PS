# 랜선 자르기

k, target = map(int, input().split())
array = []
for i in range(k):
  array.append(int(input()))
start = 1
end = max(array)

result = 0
# 랜선 길이를 이진 탐색
def binary_search(array, target, start, end):
  global result
  if start > end:
    return
  mid = (start + end) // 2
  # 해당 랜선 길이로 자름
  count = 0
  for i in array:
    count += i // mid
  if count >= target:
    result = max(result, mid)
    return binary_search(array, target, mid + 1, end)
  else:
    return binary_search(array, target, start, mid - 1)

binary_search(array, target, start, end)
print(result)