# [설탕 배달]

n = int(input())

result = 0

# 최대한 5로 담음
result += int(n / 5)
n = n % 5 

# 5로 나눈 나머지가 3으로 나누어 떨어지는지
if n % 3 == 0:
  result += n / 3
# 만약, 3으로 나누어 떨어지지 않는다면, 5를 하나씩 줄여가면서 확인
else:
  while True:
    result -= 1
    n += 5
    if result < 0:
      result = -1
      break
    if n % 3 == 0:
      result += n / 3
      break
      
print(int(result))