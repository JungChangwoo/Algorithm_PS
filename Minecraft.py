from bisect import bisect_left, bisect_right

def down_bisect(array, start, end, target):
    if start > end:
        return start
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return down_bisect(array, mid+1, end, target)
    else:
        return down_bisect(array, start, mid-1, target)

def solution(kyul):
    n = len(kyul)
    up_d = [kyul[0]]
    for i in range(1, n):
        if kyul[i] >= up_d[-1]:
            up_d.append(kyul[i])
        else:
            idx = bisect_left(up_d, kyul[i])
            up_d[idx] = kyul[i]

    down_d = [kyul[0]]
    for i in range(1, n):
        if kyul[i] <= down_d[-1]:
            down_d.append(kyul[i])
        else:
            idx = down_bisect(down_d, 0, len(down_d)-1, kyul[i])
            down_d[idx] = kyul[i]
    max_value = max(len(up_d), len(down_d))
    result = n - max_value
    return result
# [마인크래프트]
# 18111번

# 1. 현재 다 채울 수 있는 블록이 있다면 채운다.
# 2. 만약, 없다면 가장 깊은 블록부터 채워준다.
# 3. 