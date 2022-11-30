from collections import deque
def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append([progresses[i], speeds[i]])
    
    result = []
    day = 1
    count = 0
    while day < 101 and q:
        if q[0][0] + day * q[0][1] >= 100:
            count += 1
            q.popleft()
        else:
            if count > 0:
                result.append(count)
            count = 0
            day += 1
    result.append(count)
    return result