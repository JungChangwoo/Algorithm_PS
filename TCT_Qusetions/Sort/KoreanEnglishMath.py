# [국영수]
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 사전 순으로 증가하는 순서로 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옵니다)
# (1<= N <= 100,000)

n = int(input())
data = []
for i in range(n):
  data.append(list(input().split()))
print(data)

result = sorted(data, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in result:
  print(student[0])

