# [무지의 먹방 라이브]


# 개선 전
def solution(food_times, k):
    answer = 0
    index = 0
    count = 0
    while True:
        # 만약, 방송이 중단됐다면
        if count == k:
            return answer
        # 1초동안 먹는다
        food_times[index] -= 1
        # 만약, 더이상 먹을 것이 없다면
        # 가장 가까운 것 중 남은 시간이 0이 아닌 것
        for i in range(len(food_times) + 1):
            index += 1
            if index == len(food_times):
                index = 0
            if food_times[index] != 0:
                break
            if i == len(food_times):
                return -1
        answer = index + 1
        count += 1
    return answer


# 개선 후
import heapq


def solution(food_times, k):
    answer = 0
    # 만약, 전체 음식 시간보다 k가 크다면
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 Heap Queue 에 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    left_food = 0
    prev = 0

    left_food = len(food_times)

    # 가장 시간이 적은 음식부터 먹음
    while sum_value + (q[0][0] - prev) * left_food <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * left_food
        left_food -= 1
        prev = now

    # 남은 음식 중에서 몇 번째 음식인지 확인
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % left_food][1]
