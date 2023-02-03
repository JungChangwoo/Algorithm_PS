# [징검다리]
# DFS
def isPossible(mid, distance, rocks, n):
    temp = rocks[:]
    temp.append(distance)
    prev = 0
    del_count = 0
    for now in temp:
        diff = now - prev
        if diff < mid:
            del_count += 1
        else:
            prev = now
        if del_count > n:
            return False
    return True

def binary_search(start, end, rocks, n, distance):
    if start > end:
        return end
    mid = (start + end) // 2
    if isPossible(mid, distance, rocks, n):
        return binary_search(mid + 1, end, rocks, n, distance)
    else:
        return binary_search(start, mid - 1, rocks, n, distance)
    
def solution(distance, rocks, n):
    rocks.sort()
    answer = binary_search(0, distance, rocks, n, distance)
    return answer

# BFS
def isPossible2(mid, distance, rocks, n):
    temp = rocks[:]
    temp.append(distance)
    prev = 0
    del_count = 0
    for now in temp:
        diff = now - prev
        if diff < mid:
            del_count += 1
        else:
            prev = now
        if del_count > n:
            return False
    return True

def binary_search2(start, end, rocks, n, distance):
    while start <= end:
        mid = (start + end) // 2
        if isPossible(mid, distance, rocks, n):
            start = mid + 1
        else:
            end = mid - 1
    return end
    
def solution2(distance, rocks, n):
    rocks.sort()
    answer = binary_search(0, distance, rocks, n, distance)
    return answer