# 문제명 : 성적이 낮은 순서로 학생 출력
# 문제 : 학생의 성적 순으로 학생의 이름을 출력하시오. 

# # 일반적인 방식 
# n = int(input())

# array = []

# for i in range(n):
#   data = input().split()
#   array.append((data[0], int(data[1])))

# array = sorted(array, key = lambda d: d[1])

# for student in array:
#   print(student[0], end=' ')

# 계수 정렬
n = int(input())

count_array = [[] for i in range(100+1)]

for i in range(n):
  data = input().split()
  count_array[int(data[1])].append(data[0])

for i in range(len(count_array)):
  for j in count_array[i]:
    print(j, end=' ')