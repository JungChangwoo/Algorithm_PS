# 문제명 : 두 배열의 원소 교체
# 문제 : 두 배열 중 A 배열의 원소를 B 배열의 원소와 교체하여 A 배열의 모든 원소의 합이 최댓값이 되도록 하시오.

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))