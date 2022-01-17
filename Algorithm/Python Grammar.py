# 리스트
a = [i for i in range(10)]
print(a)

b = [i for i in range(10) if i%2 == 0]
print(b)

c = [[0]*9 for _ in range(9)]
print(c)

d = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in d if i not in remove_set]
print(result)
# 문자열
data = 'Hello World'
print(data)
data = "Don't you know \"Python\"?"
print(data)
# 튜플
a = (1,2,3,4)
print(a)
# 사전
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['사과'] = 'Apple2'
print(data)
data = {'사과':'Apple', '바나나': 'Banana'}
print(data)
# 집합
a = set([1,2,3,4,5])
b = {2,3,4,5,5,6}
print(a)
print(b)
print(a|b)
print(a&b)
print(a-b)
a.add(9)
a.update([5,6])
a.remove(3)
print(a)
# # 기본 입출력
# n = int(input())
# data = list(map(int, input().split()))
# # split으로 공백으로 나눈 리스트 => map으로 int형으로 바꿔줌 => list()
# data.sort()
# print(data)
# a, b, c = map(int, input().split())
# print(a,b,c)
# # 빠르게 입력받기 
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)
# f-string
answer = 7
print(f"정답은 {answer}입니다.")
print("정답은", answer, "입니다.")
# 조건문
a= 50
if a >= 90:
  pass
elif a>= 80:
  pass
else :
  print("dddd")
if a>=50 : print(a)
# Conditional Expression
score = 85
result = "Success" if score>=80 else "fail"
print(result)
a = 50
if 0 < a < 60:print(a)
# 반복문
result = 0
for i in range(1, 10):
  result += i
print(result)
# array도 가능
# continue break
# ==============================
# 함수
def add(a,b):
  return a+b #return은 없어도 된다.
print(add(1,2))
print(add(b=2, a=1))
a=0
def func():
  global a # 함수 바깥에 선언된 변수에 접근할 수 있음
  a+=1
for i in range(10): func()
print(a)
# 파이썬의 함수는 여러 개의 반환 값 가능
def fun(a,b):
  add = a+b
  sub = a-b
  return add, sub
a,b = fun(1,2)
print(a,b)
# map : 각각의 원소에 어떤 함수를 적용가능 parameter 갯수 주의
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
def add(a, b):return a+b
result = map(lambda a,b:a+b, list1, list2)
print(list(result))
# lambda 사용 x
result = map(add, list1, list2)
print(list(result))
# 자주 사용되는 내장 함수
result = sum([1,2,3,4,5])
print(result)
result = min(7,3,2,1)
print(result)
result = max(7,3,2,1)
print(result)
result = max([1,2,3,4,5])
print(result)
result = eval("(3+5)*7")
print(result)
# sorted()
result = sorted([1,5,3,2,4])
print("결과값은",result, "입니다.")
result = sorted([1,5,4,3,2], reverse = True)
print(result)
# sorted() with key
array = [('정창우',10),('정창우2''',20),('정창우3',30)]
result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)
# 순열과 조합
# 순열 : 순서고려
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data,2))
print(result)
# 조합 : 순서고려 X'
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data,2))
print(result)
# 중복 순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)
# 중복 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2))
print(result)
# Counter : 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번 등장했는지 알려줌
from collections import Counter
counter = Counter(['red', 'blue', 'red'])
print(counter['blue'])
print(counter['red'])
print(counter)
print(dict(counter))
# 최대 공약수 최소 공배수
import math
print(math.gcd(21, 14))
# print(math.lcm(21, 14))  # python 3.9
def lcm(a,b):
  return a*b // math.gcd(a,b)
print(lcm(21, 14))
