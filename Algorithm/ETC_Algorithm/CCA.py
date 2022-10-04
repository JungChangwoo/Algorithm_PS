# [좌표 압축]
# "순위가 중요한 알고리즘에서 입력값의 갯수가 입력값의 범위보다 작을 때 사용하는 방법"
# [방법]
# 입력값 범위의 배열 크기 -> 입력값 갯수 범위의 배열 크기 (0~N)
# (순위가 중요하기 때문에 값을 변경해도 상관없기 때문이다.)

# [좌표 압축]
# 18870번
import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

sorted_data = sorted(list(set(data))) # 중복 제거 and 정렬
dict = {sorted_data[i] : i for i in range(len(sorted_data))}
for i in data:
  print(dict[i], end = ' ')
