from collections import deque

graph = [1,1,1]

import copy
def test(graph):
  graph = copy.deepcopy(graph)
  graph[1] = 0

test(graph)
print(graph)