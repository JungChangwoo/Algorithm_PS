# [못생긴 수]
# 난이도: 중
# 권장 풀이 시간: 30분
# 시간 제한: 1초
# 메모리 제한: 128MB

n = int(input())

def Prime_Factor(num):
  # 약수 구함
  for i in range(1, num+1):
    if num % i == 0:
      # 소수인지
      if is_prime_number(i) == True:
        if i != 2:
          if i != 3:
            if i != 5:
              return False
  return True

d = [0 for _ in range(10000)]
def is_prime_number(x):
  if x == 1:
    return False
  if d[x] != 0:
    return d[x]
  for i in range(2, x):
    if x % i == 0:
      d[x] = False
      return d[x]
  d[x] = True
  return d[x]
  
num = 1
count = 0
while True:
  # 1부터 계속 1씩 증가하면서 해당 수의 소인수(약수 중 소수) 들을 구함
  if Prime_Factor(num) == True:
    count += 1
  if count == n:
    break;
  num += 1
  # 만약, 소인수 중 2, 3, 5 외의 숫자가 있다면 count 증가 x
  # 만약 count을 증가 했는데 n과 같다면 return 숫자
print(num)