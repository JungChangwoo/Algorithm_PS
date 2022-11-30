# [단어 변환]
from collections import deque
def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = [False] * len(words)
    while q:
        now, count = q.popleft()
        if now == target:
            return count
        for i in range(len(words)):
            if not visited[i]:
                diff = 0
                for l, r in zip(now, words[i]):
                    if l != r:
                        diff += 1
                if diff == 1:
                    visited[i] = True
                    q.append((words[i], count + 1))
    return 0