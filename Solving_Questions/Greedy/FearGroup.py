# [모험가 길드]
# 공포도가 X인 모험가는 반드시 X명 이상의 그룹에 참여해야 한다. 당신은 최대 몇 개의 모험가 그룹을 만들 수 있는가? 이때, 모든 모험가를 특정한 그룹한 넣을 필요는 없습니다.

# 나의 답 => 정답
n = int(input())
data = list(map(int, input().split()))

data.sort()

count = 0
result = 0
# 1 2 2 2 3
for i in data:
  count += 1
  if i <= count:
    count = 0
    result += 1

print(result)
