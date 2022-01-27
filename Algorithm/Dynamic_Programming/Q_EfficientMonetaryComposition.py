# 문제명 : 효율적인 화폐 구성
# 문제 : N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하시오. 이때 불가능할 때는 -1을 출력한다.

# 나의 답
n, m = map(int, input().split())
monetary = []
for i in range(n):
  monetary.append(int(input()))

d = [0] * 10001

def calMin(m):
  if m == 0: return 0
  if m < 0: return 9999
  if d[m] != 0: return d[m]
  
  d[m] = calMin(m-monetary[0]) + 1
  for i in range(1, n):
    d[m] = min(d[m], calMin(m-monetary[i]) + 1)
  return d[m]

check = False
for i in range(n):
  if m % monetary[i] == 0: check = True
if check == False: print(-1)
else: print(calMin(m))

# 이코테 답
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
data = []
for i in range(n):
  data.append(int(input()))

d = [10001] * (m+1)
# 다이나믹 프로그래밍 보텀업 방식
d[0] = 0
for i in range(n):
  for j in range(data[i], m+1):
    if d[j - data[i]] != 10001: #해당 화폐를 사용할 수 있다면
      d[j] = min(d[j], d[j-data[i]]+1) # 해당 화폐를 사용한 값과 이전의 최적의 값을 비교

if d[m] == 10001:
  print(-1)
else:
  print(d[m])

# 배운 점
# DP Table을 설계할 때, 최솟값을 구하는 것이라면 선언할 때 0이 아닌 높은 값으로 설정
# 각 값을 만들 수 있는 화폐의 사용을 어떻게 표현할 수 있을 까? => INF 탈출
# 부분 구조 : 해당 화폐를 사용해서 해당 값을 만들 수 있다면, 다른 화폐를 사용했을 때랑 비교를 해야 하겠구나 => MIN => 이는 부분 구조로 계속 보텀업으로 반복되기 때문에 최적의 값이 구해짐





