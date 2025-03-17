from collections import deque
def solution(order):
    answer = 0
    stack = []
    order = deque(order)
    n = len(order) + 1
    limit = order[0]
    for i in range(1, n):
        stack.append(i)
        left = False
        while stack:
          if stack[-1] == order[0]:
              stack.pop()
              order.popleft()
              answer += 1
              if stack and order and stack[-1] == order[0]:
                 left = True
              else:
                 left = False
          
          if not left:
            break
    print(stack, answer)
    return answer

solution([4, 3, 1, 2, 5]) #	2
# solution([5, 4, 3, 2, 1]) #	5