from collections import defaultdict
import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    my_dict = defaultdict(int)
    
    operations = [operation.split() for operation in operations]
    for operation in operations:
        oper, value = operation[0], int(operation[1])
        if oper == 'I':
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
            my_dict[value] += 1
        else:
            if value == 1:
                while max_heap:
                    value = -heapq.heappop(max_heap)
                    if my_dict[value] != 0:
                        my_dict[value] -= 1
                        break  
            else:
                while min_heap:
                    value = heapq.heappop(min_heap)
                    if my_dict[value] != 0:
                        my_dict[value] -= 1
                        break
    result = []
    for key, value in my_dict.items():
        if value != 0:
            result.append((key))
    if len(result) == 0:
        return [0, 0]
    else:
        result.sort()
        return [result[-1], result[0]]