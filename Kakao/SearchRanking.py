from collections import defaultdict
from bisect import bisect_left
from itertools import combinations


def dfs(idx, info, all_condition, condi_dict):
    if idx >= len(info) - 1:
        return
    condition = info[idx]
    condi_dict[all_condition + condition].append(int(info[-1]))
    condi_dict[all_condition + '-'].append(int(info[-1]))
    dfs(idx + 1, info, all_condition + condition, condi_dict)
    dfs(idx + 1, info, all_condition + '-', condi_dict)


def binary_search(arr, start, end, target):
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] >= target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)


def solution(infos, query):
    condi_dict = defaultdict(list)

    for info in infos:
        info = info.split()
        conditions = info[:-1]
        score = int(info[-1])
        for i in range(5):
            cases = combinations([0, 1, 2, 3], i)
            for case in cases:
                temp = conditions.copy()
                for idx in case:
                    temp[idx] = '-'
                key = ''.join(temp)
                condi_dict[key].append(score)

    for value in condi_dict.values():
        value.sort()

    answer = []
    for q in query:
        q = q.replace("and ", "")
        q = q.split()

        all_condition = ''.join(q[:-1])
        target_score = int(q[-1])

        arr = condi_dict[all_condition]

        idx = binary_search(arr, 0, len(arr) - 1, target_score)
        answer.append(len(arr) - idx)
    return answer


import bisect, itertools, collections


def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            conditions = [inf[i] if binary[i] else '-' for i in range(4)]
            key = ''.join(conditions)
            infomap[key].append(int(inf[-1]))

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        key = ''.join([l, p, c, f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers
