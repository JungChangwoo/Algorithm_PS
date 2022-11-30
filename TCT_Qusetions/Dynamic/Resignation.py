# [퇴사]
# 상담원으로 일하고 있는 백준이는 퇴사를 하려 합니다. 오늘부터 N+1일 째 되는 날 퇴사를 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 합니다. 각각의 상담은 상담을 완료하는 데 걸리는 기간 T와 받을 수 있는 금액 P로 이루어져 있습니다. 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

n = int(input())
t = []
p = []
d = [0] * (n+1)
max_value = 0

for _ in range(n):
  x, y = map(int, input().split())
  t.append(x)
  p.append(y)

for i in range(n-1, -1, -1):
  time = t[i] + i
  if time >= n:
    d[i] = max(p[i] + d[time], max_value)
    max_value = d[i]
  else:
    d[i] = max_value

print(max_value)
      

# [문제 해결 아이디어]
# d[i] = i번째 날부터 마지막 날가지 낼 수 있는 최대 이익
# max(현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤, 현재까지의 최대 상담 금액)
