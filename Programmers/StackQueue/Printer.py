from collections import deque


def solution(priorities, location):
    result = 0
    q = deque(list(enumerate(priorities)))
    while q:
        now = q.popleft()
        if any(now[1] < next[1] for next in q):
            q.append(now)
        else:
            result += 1
            if now[0] == location:
                return result
