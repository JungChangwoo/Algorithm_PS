# [효율적인 화폐 구성]
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

INF = int(1e9)
d = [INF] * 10001

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != INF:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])
