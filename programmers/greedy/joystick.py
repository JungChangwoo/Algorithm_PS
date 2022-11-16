from string import ascii_uppercase

def find_alpha_idx(alpha, target):
    for i in range(len(alpha)):
        if alpha[i] == target:
            return i
    return None

def solution(name):
    global n
    answer = 0
    arr = list(name)
    n = len(arr)
    alpha = list(ascii_uppercase)
    for i in range(len(arr)):
        left_idx = find_alpha_idx(alpha, arr[i])
        right_idx = len(alpha) - left_idx
        min_idx = min(left_idx, right_idx)
        answer += min_idx
    
    min_move = int(1e9)
    for now in range(n):
        next = now + 1
        while next < n and arr[next] == 'A':
            next += 1
        dist = min(now, n - next)
        min_move = min(min_move, now + n - next + dist)
    
    answer += min_move
    return answer