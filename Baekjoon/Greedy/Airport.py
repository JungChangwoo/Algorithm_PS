# [공항]
# 10775번
import sys
G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
gates = []
for _ in range(P):
  gates.append(int(sys.stdin.readline().rstrip()))

parent = [i for i in range(G+1)]

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

result = 0
for gate in gates:
  dock = find_parent(parent, gate)
  if parent[dock] == 0:
    print(result)
    sys.exit(0)
  parent[dock] = parent[dock - 1]
  result += 1

print(result)
  