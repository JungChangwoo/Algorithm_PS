# [1의 개수 세기]
# 9527번
import sys
import math
a, b = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**9)

def CountOne(x):
  if x <= 0:
    return 0
  n = int(math.log2(x))
  n_value = 2 ** n
  if x == n_value:
    return (n * x) // 2 + 1
  diff = x - n_value
  return CountOne(n_value) + diff + CountOne(diff)

print(CountOne(b) - CountOne(a-1))
    
