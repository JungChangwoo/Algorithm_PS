# [트리 순회]
# 1991번
import sys
from string import ascii_uppercase
n = int(sys.stdin.readline().rstrip())
alpha = list(ascii_uppercase)

graph = [[] for _ in range(n)]
for _ in range(n):
  root, left, right = sys.stdin.readline().split()
  graph[alpha.index(root)].append(left)
  graph[alpha.index(root)].append(right)
  
def preOrder(start):
  print(start, end='')
  # 왼쪽 자식이 있다면
  if graph[alpha.index(start)][0] != '.':
    preOrder(graph[alpha.index(start)][0])
  # 오른쪽 자식이 있다면
  if graph[alpha.index(start)][1] != '.':
    preOrder(graph[alpha.index(start)][1])
  return

def midOrder(start):
  # 왼쪽 자식이 있다면
  if graph[alpha.index(start)][0] != '.':
    midOrder(graph[alpha.index(start)][0])
  print(start, end='')
  # 오른쪽 자식이 있다면
  if graph[alpha.index(start)][1] != '.':
    midOrder(graph[alpha.index(start)][1])
  return

def endOrder(start):
  # 왼쪽 자식이 있다면
  if graph[alpha.index(start)][0] != '.':
    endOrder(graph[alpha.index(start)][0])
  # 오른쪽 자식이 있다면
  if graph[alpha.index(start)][1] != '.':
    endOrder(graph[alpha.index(start)][1])
  print(start, end='')
  return
  
preOrder('A')
print()
midOrder('A')
print()
endOrder('A')
