# [0-1 배날 문제: 백트래킹]
# 백트래킹: 유망하면 분기하는 방식으로 끝에 도달하면 돌아옴
# 전체 탐색의 시간 복잡도: O(2^n)
# 백트래킹의 시간 복잡도는 수학적으로 증명할 수 없으나
# pruning을 통해서 줄어들었다.
# => 백트래킹과 분기한정을 비교해서 더 빠른 것을 선택

# <유망함수>
# 1. 배낭에 아이템을 넣을 공간이 있어야한다.
# 2. 현재까지 찾은 최적 이익이 현재 노드에서 앞으로 얻을 수 있는 최대 이익보다 더 크면 유망하지 않다.
# - bound <= maxprofit
# maxprofit: 현재까지 찾은 최적해의 이익 값
# bound: 현재 노드에서 앞으로 얻을 수 있는 최대 이익
# (현재까지 이익 + 앞으로의 이익)
def promising(i, profit, weight):
  if weight > W:
    return False
  else:
    j = i + 1 # next
    bound = profit
    totweight = weight
    while j <= n and totweight + w[j] <= W:
      totweight += w[j]
      bound += p[j]
      j += 1
    k = j
    if k <= n:
      bound += (W - totweight) * (p[k] / w[k])
    return bound > maxprofit

def knapsack(i, profit, weight):
  global maxprofit, numbest, bestset
  if weight <= W and profit > maxprofit:
    maxprofit = profit
    numbest = i
    bestset = include[:] # deepcopy
  if promising(i, profit, weight):
    include[i+1] = True
    knapsack(i+1, profit + p[i+1], weight + w[i+1])
    include[i+1] = False
    knapsack(i+1, profit, weight)

n = 4
W = 16
w = [0, 2, 5, 10, 5]
p = [0, 40, 30, 50, 10]
maxprofit = 0
numbest = 0
bestset = []
include = [False] * (n+1)

knapsack(0, 0, 0)
print(bestset[1:len(bestset)])