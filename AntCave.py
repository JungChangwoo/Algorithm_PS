# [개미굴]
# 14725
import sys
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(16)]
for _ in range(n):
  data = list(sys.stdin.readline().rstrip())
  k, array = data[0], data[1:]

  