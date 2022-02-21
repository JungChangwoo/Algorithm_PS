# [문자열 뒤집기]
# 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다. 할 수 있는 행동은 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다. 문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하시오.

data = list(map(int, input()))

countA = 0
countB = 0

for i in range(len(data)-1):
  now = data[i]
  nex = data[i+1]

  if i == 0:
    if now == 1:
      countB += 1
    else:
      countA += 1

  if now != nex:
    if nex == 1:
      countB += 1
    else:
      countA += 1

result = min(countA, countB)
print(result)
  