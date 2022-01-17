# 문제 : 1이 될 때까지
# 조건 : N에서 1빼기 or N을 K로 나누기

n, k = map(int, input().split())

result = 0

while n != 1 :
  if n % k == 0:
    n //= k
    result += 1
  else :
    n -= 1
    result += 1
print(result)

# 더 최적의 복잡도
n, k = map(int, input().split())

result = 0
while True :
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k)*k
  result += (n-target) #나누어떨어지면 0
  n = target
  # N이 N보다 적을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # k로 나누기
  n //= k
  result += 1
#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)