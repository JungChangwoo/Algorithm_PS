# 문제 : 큰 수의 법칙
# 조건 : 다양한 수로 이루어진 배열이 있을 때 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징이다.

# 나의 답
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

count = 0
for i in range(0, m):
  if count < k:
    result += first
    count += 1
  else:
    result += second
    count = 0

print(result)

# 나동빈님 답
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0 : break
  result += second
  m -= 1

print(result)

# 최적화 답
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
# first 가 등장한 횟수
count = int((m / (k+1) * k))
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)

###################################################################
# 문제 해결 아이디어
# 가장 큰 수와 두 번째로 큰 수만 저장하면 된다. 
# 배운 점
# 반복되는 부분을 한 덩어리로 더 크게 생각해서 풀 수는 없을까?