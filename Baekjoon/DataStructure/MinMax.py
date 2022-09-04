# [최솟값과 최댓값]
# 2357번
import sys
n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
  array.append(int(sys.stdin.readline().rstrip()))
datas = []
for _ in range(m):
  datas.append(list(map(int, sys.stdin.readline().split())))

# 세그먼트 트리 생성
def init(node, start, end):
  if start == end:
    tree[node] = [array[start], array[start], array[start]]
    return tree[node]
  mid = (start+end)//2
  left = init(node*2, start, mid)
  right = init(node*2+1, mid+1, end)
  sum = left[0] + right[0]
  minValue = min(left[1], right[1])
  maxValue = max(left[2], right[2])
  tree[node] = [sum, minValue, maxValue]
  return tree[node]

# 구간 최소값 최대값 구하기
def subsum(node, start, end, left, right):
  if left > end or right < start:
    return [INF, 0]
  if left <= start and end <= right:
    return [tree[node][1], tree[node][2]]
  mid = (start+end)//2
  l = subsum(node*2, start, mid, left, right)
  r = subsum(node*2+1, mid+1, end, left, right)
  minValue = min(l[0], r[0])
  maxValue = max(l[1], r[1])
  return [minValue, maxValue]


INF = int(1e9)
tree = [0, INF, 0] * 200000 # 구간합, min, max
init(1, 0, n-1)
for data in datas:
  a, b = data
  result = subsum(1, 0, n-1, a-1, b-1)
  print(result[0], result[1])
  