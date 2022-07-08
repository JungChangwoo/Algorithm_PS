# [병사 배치하기]
# 난이도: 중
# 적정 풀이 시간: 40분
# 시간 제한: 1초

n = int(input())
a = list(map(int, input().split()))

a.reverse()

d = [1 for _ in range(n)]
print(d)

for i in range(1, n):
  for j in range(0, i):
    if a[j] < a[i]:
      d[i] = max(d[i], d[j]+1)

print(n - max(d))