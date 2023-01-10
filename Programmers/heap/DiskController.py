from heapq import heappush, heappop
from collections import deque
def solution(jobs):
    result = 0
    q = deque(sorted(jobs))
    h = []
    second, time = q.popleft()
    heappush(h, (time, second))
    current = 0
    while h:
        time, second = heappop(h)
        if second > current:
            current = second + time
        else:
            current += time
        result += current - second
        
        while q:
            if q[0][0] < current:
                second, time = q.popleft()
                heappush(h, (time, second))
            else:
                if not h:
                    prev = q[0][0]
                    while q:
                        next = q[0][0]
                        if prev != next:
                            break
                        second, time = q.popleft()
                        heappush(h, (time, second))
                        prev = second
    return result / len(jobs)