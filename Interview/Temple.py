# [신을 모시는 사당]
import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

def l_init(node, start, end, tree):
    if start == end:
        if array[start] == 1:
          tree[node] = 1
        else:
          tree[node] = - 1
        return tree[node]
    mid = (start + end) // 2
    left = l_init(node * 2, start, mid, tree)
    right = l_init(node * 2 + 1, mid + 1, end, tree)
    tree[node] = abs(left + right)
    return tree[node]

def r_init(node, start, end, tree):
    if start == end:
        if array[start] == 1:
          tree[node] = -1
        else:
          tree[node] = 1
        return tree[node]
    mid = (start + end) // 2
    left = l_init(node * 2, start, mid, tree)
    right = l_init(node * 2 + 1, mid + 1, end, tree)
    tree[node] = abs(left + right)
    return tree[node]

# 구간 트리 생성
l_tree = [0] * 2000001
r_tree = [0] * 2000001
l_init(1, 0, n - 1, l_tree)
r_init(1, 0, n - 1, r_tree)
print(max(max(l_tree), max(r_tree)))
