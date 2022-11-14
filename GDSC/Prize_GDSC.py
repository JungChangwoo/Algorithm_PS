from itertools import combinations
def solution(specs):
    n = len(specs)
    win = {}
    for i in range(n):
        specs[i][1], specs[i][2] = int(specs[i][1]), int(specs[i][2])
        win[specs[i][0]] = 0
    data = [i for i in range(n)]
    combs = list(combinations(data, 2))
    for comb in combs:
        left, right = comb
        left_value = specs[left][1] + specs[right][1] * specs[left][2]
        right_value = specs[right][1] + specs[left][1] * specs[right][2]
        if left_value > right_value:
            win[specs[left][0]] += 1
        elif left_value < right_value:
            win[specs[right][0]] += 1
    result = list(win.items())
    result.sort(key = lambda x: (x[1], x[0]), reverse = True)
    for i in range(n):
        result[i] = result[i][0]
    return result