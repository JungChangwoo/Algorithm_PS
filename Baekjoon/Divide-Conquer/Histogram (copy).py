# [히스토그램에서 가장 큰 직사각형]
# 6549번
import sys


# [스택]
def Histogram():
  max_size = 0
  stack = []

  for i in range(n):
    min_idx = i
    # 새로 추가될 직사각형보다 stack에 있는 것이 더 크거나 작다면
    while stack and stack[-1][1] >= rect[i]:
      # 이전의 사각형의 높이는 더이상 연속 X이므로, 왼쪽으로 갈 수 있는 길이만큼 계산하고 추출. 그리고 현재 직사각형은 마지막으로 추출된 사각형까지가 왼쪽으로 갈 수 있는 최대 길이
      min_idx, h = stack.pop()
      size = (i-min_idx) * h
      max_size = max(max_size, size)
    stack.append((min_idx, rect[i]))

  # Stack의 잔여 값 계산
  for min_idx, h in stack:
    max_size = max(max_size, h * (n-min_idx))
  return max_size
    
while True:
  n, *rect = map(int, sys.stdin.readline().split())
  if n == 0:
    break
  print(Histogram())

# [분할 정복]
def Histogram2(start, end):
    if start == end:
        return rect[start]

    mid = (start + end) // 2
    left_value = Histogram2(start, mid)
    right_value = Histogram2(mid + 1, end)

    max_val = max(left_value, right_value)

    # 중간 경계 포함 탐색
    h = min(rect[mid], rect[mid + 1])
    w = 2
    s = w * h
    left, right = mid, mid + 1
    while start < left or right < end:
        # 왼쪽으로만 갈 수 있고 더 작은 높이가 나온다면 넓이 계산
        if right == end or start < left and rect[left - 1] >= rect[right + 1]:
            left -= 1
            w += 1
            h = min(h, rect[left])
            s = max(s, w * h)
        # 오른쪽으로만 갈 수 있다면
        else:
            right += 1
            w += 1
            h = min(h, rect[right])
            s = max(s, w * h)
    # 중간 경계를 포함한 탐색과 분할 정복으로 탐색한 결과값을 비교
    max_val = max(max_val, s)

    return max_val

while True:
  n, *rect = map(int, sys.stdin.readline().split())
  if n == 0:
    break
  print(Histogram(0, n-1))