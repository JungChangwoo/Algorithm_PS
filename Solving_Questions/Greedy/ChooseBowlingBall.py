# [볼링공 고르기]
# 난이도: 하
# 권장 풀이 시간: 30분
# 시간 제한: 1초
# 메모리 제한: 128MB

# 처음 답
n, m = map(int, input().split())
ball_weighs = list(map(int, input().split()))

result = 0
for i in range(n-1):
  for j in range(i+1, n):
    if ball_weighs[i] != ball_weighs[j]:
      result += 1

print(result)

# 개선 답
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * (m+1)
for i in data:
  array[i] += 1

result = 0
for i in range(1, m+1):
  n -= array[i] # B가 선택할 수 있는 경우의 수
  result += array[i] * n # 총 경우의 수

print(result)