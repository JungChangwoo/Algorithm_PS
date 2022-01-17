# 문제명 : 음료수 얼려먹기
# 문제 : 얼음 틀에 만들 수 있는 아이스크림의 개수를 출력

# DFS로 특정 노드를 방문하고 연결된 노드들도 방문
def DFS(x, y):
  if(x<0 or x>=n or y<0 or y>=m):
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    DFS(x-1, y)
    DFS(x, y-1)
    DFS(x+1, y)
    DFS(x, y+1)
    return True
  return False

# 입력 처리
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if DFS(i, j) == True:
      result += 1

print(result)

######################################################
# 문제 해결 아이디어
# 연결되는 부분을 그래프 형태로 모델링
# => 연결되어 있는 노드를 묶음으로 처리해주는 프로그램을 어떻게 작성할 수 있을까?

# 배운점
# 간단하게 시작점에서만 계산을 해주고 나머지를 연결시키면 그 자체 하나의 덩어리로 계산할 수 있게 됨
# DFS BFS를 어떤 지점에서 활용할 것인가?