# [실패율]
# 전체 스테이지 갯수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 Stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return 하도록 solution함수를 완성하시오.
# (1 <= N <= 500)
# (1 <= Stages <= 200,000)
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 합니다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의합니다.

# 나의 답
def solution(N, stages):
    answer = []
    temp = []
    
    count = [0 for _ in range(N+1)]
    start = [0 for _ in range(N+1)]
    stagesSize = len(stages)
    
    stages.sort()
    
    for i in range(len(stages)):
        now = stages[i]
        if now > N:
            break
        if count[now] == 0:
            start[now] = i
        count[now] += 1

    for i in range(1, N+1):
        rate = count[i] / (stagesSize - start[i])
        temp.append((rate, i))
        
    temp.sort(key = lambda x : (-x[0], x[1]))
    
    for i in temp:
        answer.append(i[1])
            
    return answer


# 이코테 답
def solution2(N, stages):
  answer = []
  length = len(stages)

  for i in range(1, N+1):
    count = stages.count(i)

    if length == 0:
      fail = 0
    else:
      fail = count / length
    answer.append((i, fail))
    length -= count

  answer = sorted(answer, key=lambda x : x[1], reverser = True)

  answer = [i[0] for i in answer]
  return answer

# [배운 점]
# 문제 해결 아이디어를 너무 어렵게 생각하지 말고 필요한 단계들을 하나씩 접근
# - 해당 원소의 갯수를 구해야 함 => for (1, N+1) : COUNT
# - 실패율을 구할 때, 전체 원소의 개수에서 지금까지 나온 갯수를 뻬야 겠군 
# => 지금까지 나온 갯수 : COUNT만큼 빼줌
