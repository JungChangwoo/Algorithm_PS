# [탑승구]
# 공항에는 G개의 탑승구가 있으며, P개의 비행기가 차례대로 도착할 예정이다. i번째 비행기를 1번부터 gi번째 탑승구 중 하나에 영구적으로 도킹해야 합니다. 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있습니다. 또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 오는 경우, 그 시점에서 운행을 중지합니다. 비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하시오.
# (1 <= G <= 100,000)
# (1 <= P <= 100,000)

###########################################################3
# 나의 답
g = int(input())
p = int(input())
data = []
for _ in range(p):
  data.append(int(input()))

# 부모 테이블
parent = [0] * (g+1)
# 부모를 자기 자신으로 초기화
for i in range(1, g+1):
  parent[i] = i

# 부모 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 합집합
def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[a] = b
    return b
  else:
    parent[b] = a
    return a
    

result = 0
# 순서대로 진행
for i in range(p-1):
  # 합집합
  now = union(parent, data[i], data[i+1])
  # 만약 착륙할 탑승구가 없다면
  if data[i+1] < result:
    break
  else:
    result += 1

print(result)


############################################################
# 이코테 답
result = 0
for _ in range(p):
  data = find_parent(parent, int(input())) # 현재 비행기 탑승구의 루트 확인
  if data == 0: # 현재 루트가 0이라면, 종료
    break
  union(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
  result += 1

print(result)

# [문제 해결 아이디어]
# 가능한 큰 번호의 탑승구로 도킹을 수행한다고 가정해보자
# 도킹하는 과정을 탑승구 간 합집합 연산으로 이해할 수 있다.
# => 가장 큰 것을 먼저 선택한다고 가정하면?
# => STOP을 어떻게 설정할 것인가?
# => 합집합을 순서대로 하는데, 집합에 들어갈 자리가 없다는 것을 어떻게 설정할 것인가?
# ** 도킹하는 과정을 합집합으로 생각
# ** 들어갈 자리가 없다는 것을 루트노드의 조작으로