# 문제 : 공포도에 따라 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

# 나의 답
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0

b = list()

for i in data:
  b.append(i)
  if(len(b) >= i):
    result += 1
    b.clear()
print(result)

# 나동빈님 답
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0
print(result)
##############################################
# 문제 해결 아이디어
# 앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도가 크거나 같다면 이를 그룹으로 설정하면 된다.
# => 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 된다.
##############################################
# 배운 점
# 꼭 새로운 List를 만들 필요가 있었는지
# 어떤 방향으로 순서대로 확인해야 하는 것이라면 정렬을 사용했을 때 굉장히 코드가 간단해질 수도 있다.