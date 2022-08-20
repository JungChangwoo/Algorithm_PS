# [곱셈]
# 1629번
import sys
a, b, c = map(int, sys.stdin.readline().split())

def power(a, n):
  if n == 0:
    return 1
  if n == 1:
    return a % c
  value = power(a, n // 2)
  if n % 2 == 0:
    return (value * value) % c
  else:
    return (value * value * a) % c

print(int(power(a, b)))