from collections import deque
def solution(people, limit):
    result = 0
    people = deque([i for i in sorted(people)])
    while people:
        if len(people) == 1:
            result += 1
            people.pop()
            break
        if people[-1] + people[0] <= limit:
            result +=1
            people.popleft()
            people.pop()
        else:
            result += 1
            people.pop()
    
    return result

from collections import deque
def solution(people, limit):
    result = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
        result += 1
        right -= 1
    if left == right:
        result += 1
    return result