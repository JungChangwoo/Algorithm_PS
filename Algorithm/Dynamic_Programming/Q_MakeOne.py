# 문제명 : 1로 만들기
# 문제 : 정수 X에 대하여 다음의 4가지 연산을 사용해서 값을 1로 만들고자 합니다. 이때 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 1. X가 5로 나누어 떨어지면, 5로 나눕니다.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
# 3. X가 2로 나누어 떨어지면, 2로 나눕니다.
# 4. X에서 1을 뺍니다.
# (1 <= x <= 30,000)

x = int(input())

# 나의 답
table = [0] * 30001
def makeOne(x):
  if x == 1: return 0
  if table[x] != 0: return table[x]
  a = 9999
  b = 9999
  c = 9999
  d = 9999
  if x % 5 == 0:
    a = makeOne(x//5)
  if x % 3 == 0:
    b = makeOne(x//3)
  if x % 2 == 0:
    c = makeOne(x//2)
  d = makeOne(x-1)
  table[x] = min(a, b, c, d) + 1
  return table[x]

print(makeOne(x))
# 이코테 답
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2]+1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5]+1)

print(d[x])

# 배운 점 
# 최적 부분 구조와 중복되는 부분 문제를 만족하는가?
