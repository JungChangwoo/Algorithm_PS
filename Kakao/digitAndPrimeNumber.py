import math
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    temp = ''
    while n:
        temp += str(n % k)
        n  //= k
    temp = temp[::-1]
    
    temp = temp.split('0')
    temp = [i for i in temp if i != '']
    
    result = 0
    for number in temp:
        if is_prime(int(number)):
            result += 1
            
    return result