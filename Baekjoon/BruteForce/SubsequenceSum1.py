# [부분수열의 합]
# 1182번
import sys

n, S = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))


def DFS(i, s, num_array, include):
    global result
    if s == S and num_array > 0 and include == True:
        result += 1
    if i == n:
        return
    DFS(i + 1, s + array[i], num_array + 1, True)
    DFS(i + 1, s, num_array, False)


result = 0
DFS(0, 0, 0, False)
print(result)
