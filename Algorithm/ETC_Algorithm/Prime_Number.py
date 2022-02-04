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


