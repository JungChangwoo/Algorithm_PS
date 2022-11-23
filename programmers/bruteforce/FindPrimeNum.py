import math
def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

def dfs(value, numbers):
    if value:
        if is_prime(int(value)):
            ps.add(int(value))
    for i in range(len(numbers)):
        dfs(value + numbers[i], numbers[:i] + numbers[i+1:])
        
ps = set()
def solution(numbers):
    dfs('', numbers)
    return len(ps)