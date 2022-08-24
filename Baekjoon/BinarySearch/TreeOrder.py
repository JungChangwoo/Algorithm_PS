# [트리의 순회]
# 2263번
import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline().rstrip())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

def pre_order(inStart, inEnd, postStart, postEnd):
  if (inStart > inEnd) or (postStart > postEnd):
    return
  # postEnd = Root 를 출력
  root = post_order[postEnd]
  print(root, end=' ')
  # in_order에서 루트의 좌우로 자식들이 갈라짐
  left = positions[root] - inStart 
  right = inEnd - positions[root] 
  mid = positions[root]
  # 분할정복
  pre_order(inStart, mid -1, postStart, postStart+left-1)
  pre_order(mid + 1, inEnd, postEnd-right, postEnd-1)
  
positions = [0] * (n+1)
for i in range(n):
  positions[in_order[i]] = i
pre_order(0, n-1, 0, n-1)

 