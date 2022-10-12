# [괄호 추가하기]
# 16637번
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
data = list(sys.stdin.readline().rstrip())
for i in range(n):
  if data[i] != '+' and data[i] != '*' and data[i] != '-':
    data[i] = int(data[i])

def calculate(left, right, oper):
  if oper == '+':
    return left + right
  elif oper == '-':
    return left - right
  else:
    return left * right

def get_total(word):
  global result
  if len(word) == 1:
    print(word[0])
    sys.exit()
    return word[0]
  total = word[0]
  for i in range(1, len(word)-1, 2):
    total = calculate(total, word[i+1], word[i])
  result = max(result, total)
  
def DFS(idx, word):
  if idx >= n:
    return
  if idx == n-3:
    temp_word_1 = word[:]
    temp_word_1.append(calculate(data[idx], data[idx+2], data[idx+1]))
    get_total(temp_word_1)
    DFS(idx + 4, temp_word_1)
    temp_word_2 = word[:]
    temp_word_2 += data[idx:idx+2]
    DFS(idx + 2, temp_word_2)
    return
  if idx == n-1:
    word.append(data[idx])
    get_total(word)
    return 
  # 괄호를 추가하는 경우
  temp_word_1 = word[:]
  temp_word_1.append(calculate(data[idx], data[idx+2], data[idx+1]))
  temp_word_1 += data[idx + 3]
  DFS(idx + 4, temp_word_1)
  # 괄호를 추가하지 않는 경우
  temp_word_2 = word[:]
  temp_word_2 += data[idx:idx+2]
  DFS(idx + 2, temp_word_2)

result = -(10**9)
DFS(0, [])
print(result)
  