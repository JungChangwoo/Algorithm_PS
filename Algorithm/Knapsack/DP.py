# [0-1 배낭 문제: 동적 계획법]

# [동적 계획법]
# 1. 재귀 관계식
# p[i][w]: 총 무게가 w를 초과하지 않으며 i개의 아이템에서만 선택했을 때 최대 이익
# if wi <= w => max(p[i-1][w], p[i-1][w-wi] + pi)
# else => p[i-1][w]
# 시간복잡도: O(nW)
# => W가 크면 문제가 생김


# [효율적인 동적 계획법]
# p[n][w]를 계산하려면 p[n-1][w], p[n-1][w-wn]만 필요
# p[i][w]를 계산하려면 p[i-1][w], p[i-1][w-wi]만 필요
# => 재귀 호출 (공간자체를 만들지 않는다.)
def knapsack(i, W, w, p):
    if i <= 0 or W <= 0:
        return 0
    if w[i] > W:
        return knapsack(i - 1, W, w, p)
    else:
        left = knapsack(i - 1, W, w, p)
        right = knapsack(i - 1, W - w[i], w, p)
        return max(left, right + p[i])


# [기본 동적 계획법]
def knapsack2(P):
    for i in range(n + 1):
        P[i][0] = 0
    for j in range(1, W + 1):
        P[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # 담을 수 없다면
            if w[i] > j:
                P[i][j] = P[i - 1][j]
            # 담을 수 있다면
            else:
                P[i][j] = max(P[i - 1][j], p[i] + P[i - 1][j - w[i]]) # 담는 것과 담지 않는 것 중 더 최적의 값을 선택


W = 30
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
n = 3
P = [[0] * (W + 1) for _ in range(n + 1)]
result = knapsack(len(w) - 1, W, w, p)
result2 = knapsack2(P)
print(result)
print(P)
