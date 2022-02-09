# [소수 (Prime Number)]
# - 코딩 테스트에서는 어떠한 자연수가 소수인지 아닌지 판별해야 하는 문제가 자주 출제된다.
# <기본적인 알고리즘>
# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False 
  return True

print(is_prime_number(4))
print(is_prime_number(7))
# => 시간 복잡도 O(X)
# <개선된 알고리즘)
# - 모든 약수는 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
import math

def is_prime_number2(x):
  for i in range(2, int(math.sqrt(x)) +1):
    if x % i == 0:
      return False
  return True

print(is_prime_number(4))
print(is_prime_number(7))
# => 시간복잡도 O(X^1/2) 
# 2부터 X의 제곱근까지의 반복만 수행하면 됨

# [다수의 소수 판별]
# <에라토스테네스의 체 알고리즘>
# 1. 2부터 N까지의 모든 자연수를 처리한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 소가 소수(True)인 것으로 초기화한다.(0과 1은 제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 N의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True: # i가 소수인 경우
    # i를 제외한 i의 모든 배수를 지우기
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

# 모든 소수 출력
for i in range(2, n+1):
  if array[i]:
    print(i, end=' ')

# <성능 분석>
# 시간 복잡도 : O(NloglogN)

