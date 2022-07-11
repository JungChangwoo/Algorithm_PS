# [연산자 끼워 넣기]
# 난이도: 중상
# 권장 풀이 시간: 30분
# 시간 제한: 2초
# 메모리 제한: 512MB

n = int(input())
data = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

result = []
def DFS(i, now):
  global add, minus, mul, div
  
  if i == n-1:
    result.append(now)

  if add > 0:
    add -= 1
    DFS(i+1, now + data[i+1])
    add += 1
  if minus > 0:
    minus -= 1
    DFS(i+1, now - data[i+1])
    minus += 1
  if mul > 0:
    mul -= 1
    DFS(i+1, now * data[i+1])
    mul += 1
  if div > 0:
    div -= 1
    DFS(i+1, int(now / data[i+1]))
    div += 1
  
DFS(0, data[0])

print(max(result))
print(min(result))
# ============================================
n = int(input())
data = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = int(-1e9)
def DFS(i, now):
  global add, minus, mul, div, min_value, max_value
  
  if i == n-1:
    min_value = min(min_value, now)
    max_value = max(max_value, now)

  if add > 0:
    add -= 1
    DFS(i+1, now + data[i+1])
    add += 1
  if minus > 0:
    minus -= 1
    DFS(i+1, now - data[i+1])
    minus += 1
  if mul > 0:
    mul -= 1
    DFS(i+1, now * data[i+1])
    mul += 1
  if div > 0:
    div -= 1
    DFS(i+1, int(now / data[i+1]))
    div += 1
  
DFS(0, data[0])

print(max_value)
print(min_value)