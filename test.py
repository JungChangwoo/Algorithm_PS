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
    return str(self.a) + str(self.b)
q = []
heapq.heappush(q, node(1,-1))
heapq.heappush(q, node(1, 1))
heapq.heappush(q, node(2, 2))
heapq.heappush(q, node(2, -2))
while q:
  print(heapq.heappop(q))