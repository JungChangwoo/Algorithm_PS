# [부분수열의 합 2]
# 1208번

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

# ㅔ