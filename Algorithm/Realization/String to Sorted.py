# 문제 : 알파벳 대문자와 숫자로만 이루어진 문자열을 받은 뒤, 알파벳은 오름차순으로 정렬하여 출력한 뒤 숫자는 모두 더한 값을 출력

# 나의 답
data = input()

num = 0
s = ""
for i in data:
  if 48<= ord(i) <=57:
    num += int(i)
  if 65<= ord(i) <=90:
    s += i

result = "".join(sorted(list(s))) + str(num)
print(result)
# 나동빈님 답 
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print("".join(result))

################################################################################### 배운 점 
# 파이썬의 내장 함수를 잘 알고 있을 수록 편하다