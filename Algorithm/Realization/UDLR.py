# 문제 : 상하좌우
# 조건 : 공간을 벗어나는 움직임은 무시한다. 

n = int(input())
data = list(input().split())

# 서동북남
dx = [0, 0, -1 , 1] #행
dy = [-1, 1, -0, 0] #열

d = ['L', 'R', 'U', 'D']

resultX = 1
resultY = 1

for i in data:
  direction = d.index(i)
  print(direction)
  nx = resultX + dx[direction] 
  ny = resultY + dy[direction]

  if nx<1 or ny <1 or nx>n or ny>n: #공간을 벗어나는 경우 무시
    continue
  #이동수행
  resultX, resultY = nx, ny

print(resultX, resultY)

##############################################################################################
# 배운 점
# 방향 벡터와 Move_Type의 정의
# 계산을 한 후 검증을 해야 할 때, 임시 변수에 담아두었다가 끝난 후에 담아주면 편하다
# => 검증 후 continue or 실제 값에 임시 값을 담아줌 