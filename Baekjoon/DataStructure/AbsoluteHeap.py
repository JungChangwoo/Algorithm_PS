# [절댓값 힙]
# 11286번
import sys
import heapq

class node:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __lt__(self, other):
    if self.a < other.a:
      return True
    elif self.a == other.a:
      return self.b < other.b
    else:
      return False
  def __str__(self):
    return str(self.b)

n = int(sys.stdin.readline().rstrip())
q = []
for _ in range(n):
  inp = int(sys.stdin.readline().rstrip())
  if inp != 0:
    heapq.heappush(q, node(abs(inp), inp))
  else:
    if len(q) == 0:
      print(0)
      continue
    else:
      print(heapq.heappop(q))
