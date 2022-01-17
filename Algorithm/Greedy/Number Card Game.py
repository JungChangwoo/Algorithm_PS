# 문제 : 숫자 카드 게임 (가장 큰 수의 카드를 뽑는다)
# 조건 : 행을 선택한 뒤, 해당 행에서 가장 작은 값을 뽑아야 한다.

n, m = map(int, input().split())


result = 0

for i in range(n):
  row = list(map(int, input().split()))
  min_value = min(row)
  result = max(result, min_value)

print(result)

############################################################
# 배운 점
# 가장 큰 값 or 가장 작은 값을 얻고자 할 때, 계속 비교해가며 답에 근접한 변수를 하나 설정하면 간단해진다. 