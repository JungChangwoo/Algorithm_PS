# [문자열 재정렬]
# 알파벳과 숫자로 이루어진 문자열이 들어왔을 때, 문자열을 오름차순으로 정렬하여 보여주고 이어서 모든 숫자를 더한 값을 출력하시오.
# (1 <= 문자열 길이 <= 10,000)
# 시간 제한 : 1초

data = input()

alpha = []
result = 0

for i in data:
  if i.isalpha():
    alpha.append(i)
  else:
    result += int(i)

alpha.sort()
alpha.append(str(result))

print(''.join(alpha))