# [소트인사이드]
# 문제 번호: 1427

data = list(map(int, input()))
count_sort = [0] * 10
for i in data:
  count_sort[i] += 1

result = ''
for i in range(len(count_sort)-1, -1, -1):
  for _ in range(count_sort[i]):
    result += str(i)

print(result)