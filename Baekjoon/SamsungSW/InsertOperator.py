# [연산자 끼워넣기]
# 14888번

n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split())) # 덧셈 뺄셈 곱셈 나눗셈

max_value = -int(1e9)
min_value = int(1e9)
def DFS(value, idx):
  global max_value, min_value
  # 모든 연산자를 대입했을 경우에 값 계산해서 결과 리스트에 담아줌
  if idx == n-1:
    max_value = max(max_value, value)
    min_value = min(min_value, value)
    return
  # 현재 가능한 연산자로 계산을 해줌
  if oper[0] > 0:
    oper[0] -= 1
    DFS(value + data[idx + 1], idx + 1)
    oper[0] += 1
  if oper[1] > 0:
    oper[1] -= 1
    DFS(value - data[idx + 1], idx + 1)
    oper[1] += 1
  if oper[2] > 0:
    oper[2] -= 1
    DFS(value * data[idx + 1], idx + 1)
    oper[2] += 1
  if oper[3] > 0:
    oper[3] -= 1
    DFS(int(value / data[idx + 1]), idx + 1)
    oper[3] += 1

DFS(data[0], 0)
print(max_value)
print(min_value)


