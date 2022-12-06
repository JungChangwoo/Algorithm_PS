import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while scoville:
        left = heapq.heappop(scoville)
        if left >= K:
            return result
        if len(scoville) == 0:
            return -1
        right = heapq.heappop(scoville)
        heapq.heappush(scoville, left + right * 2)
        result += 1