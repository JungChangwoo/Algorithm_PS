import itertools


def solution(n, weak, dist):
    weak += list(map(lambda x: x + n, weak[:]))
    result = int(1e9)

    for start in range(len(weak) // 2):

        cases = list(itertools.permutations(dist, len(dist)))
        for case in cases:
            c_idx = 0
            w_idx = start
            length = weak[w_idx] + case[c_idx]

            while w_idx - start < len(weak) // 2:
                if length < weak[w_idx]:
                    c_idx += 1
                    if c_idx == len(dist):
                        c_idx = int(1e9)
                        break
                    length = weak[w_idx] + case[c_idx]
                w_idx += 1

            result = min(result, c_idx + 1)

    if result == int(1e9):
        return -1
    return result
