# [택배 배달과 수거하기]

# 나의 풀이
def solution(cap, n, deliveries, pickups):
    result = 0
    idx = n - 1
    d_idx, p_idx = idx, idx
    while idx >= 0:
        d_first, p_first = -1, -1
        d_cap, p_cap = cap, cap
        while d_cap > 0 and d_idx >= 0:
            if deliveries[d_idx] > 0:
                if d_first == -1:
                    d_first = d_idx
                if deliveries[d_idx] >= d_cap:
                    deliveries[d_idx] -= d_cap
                    d_cap = 0
                    break
                else:
                    d_cap -= deliveries[d_idx]
                    deliveries[d_idx] = 0
            d_idx -= 1
        while p_cap > 0 and p_idx >= 0:
            if pickups[p_idx] > 0:
                if p_first == -1:
                    p_first = p_idx
                if pickups[p_idx] >= p_cap:
                    pickups[p_idx] -= p_cap
                    p_cap = 0
                    break
                else:
                    p_cap -= pickups[p_idx]
                    pickups[p_idx] = 0
            p_idx -= 1
        distance = (max(d_first, p_first)+1) * 2
        result += distance
        idx = max(d_idx, p_idx)
        if p_idx < 0 and d_idx < 0:
            break
        
    return result

# 참조 풀이
def solution(cap, n, deliveries, pickups):
    result = 0
    d, p = 0, 0
    idx = n-1
    for i in range(n-1, -1, -1):
        if deliveries[i] > 0 or pickups[i] > 0:
            idx = i
            break
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        while d > cap or p > cap:
            d -= cap
            p -= cap
            result += (idx + 1) * 2
            idx = i
            
    if p > 0 or d > 0:
        result += (idx + 1) * 2
    return result