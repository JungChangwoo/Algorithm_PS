# 문제 : 곱하기 혹은 더하기
# 조건 : 왼쪽부터 X or + 가장 큰 값
data = input()

result = int(data[0])
for i in range(1, len(data)):
  num = int(data[i])
  if(result <=1 or num <=1):
    result += num
  else:
    result *= num
print(result)
####################################
# 1보다 작을 때의 예외사항을 떠올릴 수 있어야함
# 1보다 작은 케이스를 Prev 값과 현재 값이라는 것