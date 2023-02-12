def solution(orders, course):
    result = []
    
    for c in course:
        comb_dict = defaultdict(int)
        
        for order in orders:
            combs = list(combinations(order, c))
            for comb in combs:
                comb = list(comb)
                comb.sort()
                comb_dict[''.join(s for s in comb)] += 1
                
        if comb_dict:
            sorted_dict = sorted(comb_dict.items(), key = lambda x: x[1], reverse=True)
            max_value = sorted_dict[0][1]
            for key, value in sorted_dict:
                if value == max_value and value >= 2:
                    result.append(key)
                else:
                    break
            
    result.sort()
    return result

from itertools import combinations
import collections
def solution(orders, course):
    result = []
    
    for c in course:
        order_combs = []
        
        for order in orders:
            order_combs += combinations(sorted(order), c)
                
        count_ordered = collections.Counter(order_combs).most_common()
        for co in count_ordered:
            if co[1] > 1 and co[1] == count_ordered[0][1]:
                result.append(''.join(s for s in co[0]))
            else:
                break
                
    result.sort()
    return result