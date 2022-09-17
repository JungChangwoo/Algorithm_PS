import sys

n, m, k = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline().rstrip()))


def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    mid = (start + end) // 2
    left = init(node * 2, start, mid)
    right = init(node * 2 + 1, mid + 1, end)
    tree[node] = left + right
    return tree[node]


def get_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_sum = get_sum(node * 2, start, mid, left, right)
    right_sum = get_sum(node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


# 구간 트리 생성
tree = [0] * 4000000
init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - array[b - 1]
        array[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    else:
        result = get_sum(1, 0, n - 1, b - 1, c - 1)
        print(result)
