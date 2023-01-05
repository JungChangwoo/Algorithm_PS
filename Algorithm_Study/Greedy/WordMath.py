# [단어 수학]
# 1339번
import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
words = []
my_dict = defaultdict(int)
for _ in range(n):
  word = list(sys.stdin.readline().rstrip())
  words.append(word)
  temp = 1
  for i in range(len(word)-1, -1, -1):
    my_dict[word[i]] += temp
    temp *= 10

sorted_dict = dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = True))
temp = 9
for alpha, value in sorted_dict.items():
  sorted_dict[alpha] = temp
  temp -= 1
  
total = 0
for word in words:
  value = ''
  for i in word:
    value += str(sorted_dict[i])
  total += int(value)
print(total)
