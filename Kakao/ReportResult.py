from collections import defaultdict
def solution(id_list, report, k):
    r_dict = defaultdict(list)
    c_dict = defaultdict(int)
    
    for r in set(report):
        a, b = r.split()
        r_dict[a].append(b)
        c_dict[b] += 1
        
        
    result = [0] * len(id_list)
    for i, a in enumerate(id_list):
        value = 0
        for b in r_dict[a]:
            if c_dict[b] >= k:
                value += 1
        result[i] = value
    return result


from collections import defaultdict
def solution(id_list, report, k):
    c_dict = defaultdict(int)
    report = set(report)
    
    for r in report:
        a, b = r.split()
        c_dict[b] += 1
        
        
    result = [0] * len(id_list)
    for r in report:
        a, b = r.split()
        if c_dict[b] >= k:
            result[id_list.index(a)] += 1
    return result