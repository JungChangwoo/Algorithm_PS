# [골드바흐의 추측]
# 9020번
import sys, math
n = 10000
array = [True] * (n+1)
for i in range(2, int(math.sqrt(n)) +1):
  if array[i]:
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

prime = []
for i in range(2, n+1):
  if array[i]:
    prime.append(i)
      
for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  result = int(1e9)
  result_i = 0
  result_j = 0
  i = 0
  while prime[i] < n:
    j = i
    while prime[j] < n:
      if prime[i] + prime[j] == n:
        if result >  prime[j] - prime[i]:
          result_i = prime[i]
          result_j = prime[j]
          result = prime[j] - prime[i]
      j += 1
      if j >= len(prime):
        break
    i += 1
    if i >= len(prime):
      break
  print(result_i, result_j)

import sys, math
n = 10000
array = [True] * (n+1)
for i in range(2, int(math.sqrt(n)) + 1):
  if array[i]:
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1 
    
for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  left = n // 2
  right = n // 2
  while True:
    while array[left] == False or left + right > n:
      left -= 1
    while array[right] == False or left + right < n:
      right += 1
    if left + right == n:
      break
  
  print(left, right)
        
      
        
  
  