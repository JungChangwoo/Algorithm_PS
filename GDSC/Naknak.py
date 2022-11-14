def solution(buildings):
    nak = ['n', 'a', 'k']
    result = []

    for building in buildings:
        idx = 0
        count = 0
        for i in building:
            if i == nak[idx]:
                idx += 1
            if idx == 3:
                idx = 0
                count += 1
        if count == 2:
            result.append('O')
        else:
            result.append('X')
    return result