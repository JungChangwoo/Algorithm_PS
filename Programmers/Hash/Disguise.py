from collections import defaultdict
from functools import reduce
def solution(clothes):
    my_dict = defaultdict(int)
    for name, category in clothes:
        my_dict[category] += 1
    return reduce(lambda x, y: x * (y+1), my_dict.values(), 1) - 1

from collections import Counter
from functools import reduce
def solution(clothes):
    counter = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y: x * (y+1), counter.values(), 1) - 1