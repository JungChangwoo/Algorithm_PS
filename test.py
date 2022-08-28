from bisect import bisect_left, bisect_right
array = [2, 5, 10]

def binary_search(array, target, start, end):
  if start > end:
    return start
  mid = (start+end) // 2
  if array[mid] == target:
    return mid
  if array[mid] < target:
    return binary_search(array, target, mid+1, end)
  else:
    return binary_search(array, target, start, mid-1)

print(binary_search(array, -1, 0, 2))