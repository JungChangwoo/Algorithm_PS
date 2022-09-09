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
    return knapsack(i-1, W, w, p)
  else:
    left = knapsack(i-1, W, w, p)
    right = knapsack(i-1, W-w[i], w, p)
    return max(left, right + p[i])


W = 30
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
result = knapsack(len(w)-1, W, w, p)
print(result)
