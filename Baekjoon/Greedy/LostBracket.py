# [잃어버린 괄호]
# 1541번
import sys
data = sys.stdin.readline().rstrip()
array = []
string = ""
for i in range(len(data)):
  if i == len(data) - 1:
    string += data[i]
    array.append(string)
  if data[i] != "-" and data[i] != "+":
    string += data[i]
  else:
    array.append(string)
    array.append(data[i])
    string = ""

result = 0
isMinus = False
for i in range(len(array)):
  if array[i] == '+':
    continue
  # 만약 -가 나오면
  if array[i] == '-':
    isMinus = True
    continue
  if isMinus == False:
    result += int(array[i])
  else:
    result -= int(array[i])
print(result)