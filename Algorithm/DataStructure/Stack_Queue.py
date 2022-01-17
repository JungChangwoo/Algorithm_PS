# 큐(Queue)
##################################################
# deque는 스택과 큐의 장점을 모두 채택한 것으로 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이다.

from collections import deque
# 큐(Queue) 구현을 위해 deque라이브러리 사용
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

queue.reverse()
print(queue)

# 스택(Stack)
##################################################
# 스택은 파이썬에서 제공해주는 리스트로 같은 기능을 할 수 있다.
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print(stack)