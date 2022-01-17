# 문제 : 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 구하시오.

# 나의 답 ==> 오답
n = int(input())

include = False
result = 0

for i in range(n+1):
  if '3' in str(i): include = True
  for j in range(60):
    if '3' in str(j): include = True
    for k in range(60):
      if '3' in str(k): include = True
      if include == True: result += 1
  include = False

print(result)

# 나동빈님 답
h = int(input())

count = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count += 1

print(count)

###################################################################
# 문제 해결 아이디어
# 하루는 86,400 초로, 모든 경우의 수를 계산해도 2초 안에 문제를 해결할 수 있다. => 3중 반복문을 사용하여 모든 경우의 수를 체크한다.
# 배운 점
# 이전의 값이 오염되기 때문에, 마지막에 한번에 검증했어야 한다. 
# 각 문자열들이 있고, 어떤 하나의 존재에 따라서 결과가 결정되는 경우 문자열을 하나로 합쳐서 생각해보자.