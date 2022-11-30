# [가사 검색]
# 난이도: 상
# 풀이 시간: 1시간 30분

# 나의 답: 오답
# => 정확성 O But 효율성에서 감점당함 
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    words.sort(key=lambda x: len(x))

    words_length = []
    for word in words:
      length = len(word)
      words_length.append(length)

    for query in queries:
        count = 0
        
        query_length = len(query)
        left_index = bisect_left(words_length, query_length)
        right_index = bisect_right(words_length, query_length)
        
        validation_array = []
        validation_index = 0
        validation_direction = 0 
        
        if(query[0] == '?'):
            for i in range(len(query)):
                if query[i] != '?':
                    validation_index = i
                    validation_direction = 0
                    break;
        else:
            for i in range(len(query)-1, 0, -1):
                if(query[i] != '?'):
                    validation_index = i
                    validation_direction = 1
                    break;
        if validation_direction == 0:
            for i in range(validation_index, len(query)):
                validation_array.append(query[i])
        else:
            for i in range(0, validation_index+1):
                validation_array.append(query[i])

        if validation_direction == 0:
          for i in range(left_index, right_index):
            words_string = words[i]
            isOk = True
            for i in range(len(validation_array)):
              if validation_array[i] != words_string[i+validation_index]:
                isOk = False
            if isOk == True:
              count += 1
        else:
          for i in range(left_index, right_index):
              words_string = words[i]
              isOk = True
              for i in range(len(validation_array)):
                  if validation_array[i] != words_string[i]:
                      isOk = False
              if isOk == True:
                  count += 1
                
        answer.append(count)
    return answer

# 이코테 답
from bisect import bisect_left, bisect_right

def count_by_value(a, left_value, right_value):
  left_index = bisect_left(a, left_value)
  right_index = bisect_right(a, right_value)
  return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution2(words, queries):
  answer = []
  # 길이별로 분류
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])
  # 정렬
  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  # 쿼리 반복 실행
  for q in queries:
    res = 0
    if q[0] != '?':
      res = count_by_value(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
    else:
      res = count_by_value(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
    answer.append(res)
  return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution2(words, queries))

# [문제 해결 아이디어]
# 시간 복잡도 계산 철저히
# 이진 탐색을 어떤 부분에 어떻게 활용할 것인가
# 파이썬 문법 이해
# => 이진 탐색을 효과적이지 않은 곳에 적용하여 실패했다.
# => 이진 탐색을 사용해야 하는 부분을 정확히 찾고 어떻게 하면 해당 부분에 적용할 수 있을지 고민