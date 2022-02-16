# [곱하기 혹은 더하기]
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 + 혹은 x 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
# (1 <= S의 길이 <= 20)
# 시간 제한 : 1초

data = input()
s = []
for i in data:
  s.append(int(i))

result = 0

for i in range(len(s)-1):
  nex = s[i+1]
  if i==0:
    result += s[i]
  if result == 0 or nex == 0 or result == 1 or nex == 1:
    result = result + nex
  else:
    result = result * nex

print(result)
#################################################################################
data = input()
s = []
for i in data:
  s.append(int(i))

result = s[0]

for i in range(1, len(s)):
  num = s[i]
  if result <=1 or num <=1:
    result += num
  else:
    result *= num

print(result)