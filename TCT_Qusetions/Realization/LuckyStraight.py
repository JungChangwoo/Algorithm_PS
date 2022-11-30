# [럭키 스트레이트]
# 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황인지 아닌지를 알려주는 프로그램을 작성하시오. 이때, 점수 N의 자릿수는 항상 짝수 형태로만 주어집니다.abs
# - (10 <= N <= 99,999,999)

# 나의 답
n = list(map(int, input()))

a = n[0:(len(n)//2)]
b = n[len(n)//2:]

equal = 0
for i in a:
  equal += i

result = 'Ready'
value = 0

b.sort(reverse=True)
for i in b:
  if i > equal:
    break
  value += i
if value == equal:
  result = 'LUCKY'

print(result)

# 이코테 답
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i])
for i in range(length // 2, length):
  summary -= int(n[i])

if summary == 0:
  print("LUCKY")
else:
  print("READY")
