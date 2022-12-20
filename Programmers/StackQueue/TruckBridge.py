# [다리를 건너는 트럭]
# 모든 트럭이 다리를 건너는 최소 시간을 구하시오
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bq = deque([0] * bridge_length)
    tq = deque(truck_weights)
    temp, result = 0, 0
    while bq:
        result += 1
        temp -= bq.popleft()
        if tq:
            if temp + tq[0] <= weight:
                temp += tq[0]
                bq.append(tq[0])
                tq.popleft()
            else:
                bq.append(0)
    return result
