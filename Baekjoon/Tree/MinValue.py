# [최솟값]
# 10868번
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
  array.append(int(sys.stdin.readline().rstrip()))

def init_tree(node, start, end):
  if start == end:
    tree[node] = array[start]
    return tree[node]
  mid = (start + end) // 2
  tree[node] = min(init_tree(node*2, start, mid), init_tree(node*2+1, mid+1, end))
  return tree[node]

def get_min(node, start, end, left, right):
  if left > end or right < start:
    return INF
  if left <= start and right >= end:
    return tree[node]
  mid = (start + end) // 2
  return min(get_min(node*2, start, mid, left, right), get_min(node*2+1, mid+1, end, left, right))

tree = [0] * (2**18)
INF = int(1e9)
init_tree(1, 0, n-1)
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(get_min(1, 0, n-1, a-1, b-1))