# [괄호 변환]
# 2020 Kakao Blind Recruitment
def divide_idx(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return i
    return 0

def reverse(p):
    temp = ''
    for i in p:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp

def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
    return True

def DFS(p):
    p = p[:]
    if p == '':
        return ''
    idx = divide_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check(u):
        u += DFS(v)
        return u
    else:
        temp = '('
        temp += DFS(v)
        temp += ')'
        temp += reverse(u[1:-1])
        return temp 

def solution(p):
    if check(p):
        return p
    result = DFS(p)
    return result