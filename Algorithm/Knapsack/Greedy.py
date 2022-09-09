# 아이템이 분할 가능할 때만 그리디가 최적 해 보장
# else => dp, back-tracking, 분기한정
def knapsack(W, w, p):
    n = len(w) - 1
    k = [0] * (n + 1)
    weight = 0
    for i in range(1, n + 1):
        weight += w[i]
        k[i] = w[i]
        if weight > W:
            k[i] -= weight - W
            break
    return k


w = [0, 2, 5, 8, 7, 40, 13, 24]  # 수량
p = [0, 15, 12, 8, 8, 7, 5, 2]  # kg당 가격
W = 30
k = knapsack(W, w, p)
print(k, sum(k))
price = 0
for i in range(1, len(k)):
    price += p[i] * k[i]
print(price)
