# [큰 수 만들기]
def solution(number, k):
    n = len(number)
    stack = []
    for i, value in enumerate(number):
        while stack and k > 0 and stack[-1] < value:
            stack.pop()
            k -= 1
        stack.append(value)
    return ''.join(s for s in stack[:n-k])