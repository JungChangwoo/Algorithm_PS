# [입국심사]
def solution(n, times):
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start
