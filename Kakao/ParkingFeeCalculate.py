from collections import defaultdict
import math
def to_second(clock):
    minute, second = clock.split(':')
    return int(minute) * 60 + int(second)

def solution(fees, records):
    diff_dict = defaultdict(int)
    
    visited = [False] * len(records)
    for i, record in enumerate(records):
        now, num, oper = record.split()
        now = to_second(now)
        
        if oper == 'OUT':
            for j, record2 in enumerate(records[:i]):
                prev, num2, oper2 = record2.split()
                prev = to_second(prev)
                if num2 == num and oper2 == 'IN' and not visited[j]:
                    diff_dict[num2] += now - prev
                    visited[j] = True
                    break
                    
    for i, record in enumerate(records):
        now, num, oper = record.split()
        if oper == 'IN' and not visited[i]:
            now = to_second(now)
            end = to_second('23:59')
            diff_dict[num] += (end - now)
    
    diffs = sorted(list(diff_dict.items()))
    result = []
    for num, second in diffs:
        if second <= fees[0]:
            result.append(fees[1])
        else:
            total = fees[1] + (math.ceil((second - fees[0]) / fees[2])) * fees[3]
            result.append(total)
            
    return result