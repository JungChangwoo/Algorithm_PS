import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001


def BFS():
    global result_cost, result_case
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        now = q.popleft()
        if now == k:
            result_cost = visited[now]
            result_case += 1
        if result_cost != -1 and visited[now] > result_cost:
            break
        for next in (now + 1, now - 1, now * 2):
            if 0 <= next < 100001:
              if visited[next] == -1 or visited[next] == visited[now] + 1:
                visited[next] = visited[now] + 1
                q.append(next)


result_cost = -1
result_case = 0
BFS()
print(result_cost)
print(result_case)
