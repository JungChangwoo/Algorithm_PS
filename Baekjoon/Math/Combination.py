# [조합]
# 2407번 

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

def getCombinations(n, m):
  valueA = 1
  for i in range(1, n+1):
    valueA *= i
  valueB = 1
  for i in range(1, m+1):
    valueB *= i
  valueC = 1
  for i in range(1, n-m+1):
    valueC *= i
  return valueA // (valueB * valueC)
print(getCombinations(n, m))