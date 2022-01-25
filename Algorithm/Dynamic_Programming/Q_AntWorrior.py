# 문제명 : 개미 전사
# 문제 : 개미가 메뚜기 마을의 식량창고를 공격하려고 하는데, 들키지 않으려면 최소 한 칸 이상 떨어진 창고를 약탈해야 한다. 이때 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.

n = int(input())
warehouse = list(map(int, input().split()))

d = [0] * 100

d[0] = warehouse[0]
d[1] = max(warehouse[0], warehouse[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2]+warehouse[i])

print(d[n-1])

# 배운 점
# - 다이나믹 프로그래밍이라고 생각되면, 점화식을 먼저 생각할 것
# - 어디까지 고려를 해야하는 것인지(i-3은 고려할 필요가 없다)
# - 탈출을 어떻게 할 것인지 or 시작을 어떻게 할 것인지