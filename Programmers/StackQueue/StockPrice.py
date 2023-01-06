# [주식가격]
def solution(prices):
    stack = []
    result = [0] * len(prices)
    for idx, price in enumerate(prices):
        while stack:
            if stack[-1][0] > price:
                t_price, t_idx = stack.pop()
                result[t_idx] = idx - t_idx
            else:
                break
        stack.append([price, idx])
    while stack:
        price, idx = stack.pop()
        result[idx] = len(prices) - idx - 1
    return result