import math
def to_tree(number):
    binary = format(number, 'b')
    height = int(math.log2(len(binary))) + 1
    count = 2 ** height - 1
    return '0' * (count - len(binary)) + binary

def isPossible(tree, parent):
    if parent == '0':
        for child in tree:
            if child == '1':
                return False
            
    if len(tree) == 1:
        return True
    
    mid = len(tree) // 2
    return isPossible(tree[:mid], tree[mid]) and isPossible(tree[mid+1:], tree[mid])

def solution(numbers):
    answer = []
    for number in numbers:
        tree = to_tree(number)
        if isPossible(tree, tree[len(tree) // 2]):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

import math
def to_tree(number):
    binary = format(number, 'b')
    height = int(math.log2(len(binary))) + 1
    count = 2 ** height - 1
    return '0' * (count - len(binary)) + binary

def isPossible(tree, start, end):
    if start >= end:
        return tree[start]
    
    mid = (start + end) // 2
    
    left = isPossible(tree, start, mid - 1)
    if not left or tree[mid] == '0' and left == '1':
        return False
    
    right = isPossible(tree, mid + 1, end)
    if not right or tree[mid] == '0' and right == '1':
        return False
    
    return tree[mid]

def solution(numbers):
    answer = []
    for number in numbers:
        tree = to_tree(number)
        if isPossible(tree, 0, len(tree) - 1):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer