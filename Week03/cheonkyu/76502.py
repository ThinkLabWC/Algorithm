from collections import deque
def solution(s):
    answer = 0
    q = deque(list(s))
    n = len(s)
    while n:
        stack = []
        str_list = list(q)
        for s in str_list:
            if stack:
              if stack[-1] == '[' and s == ']':
                  stack.pop()
                  continue
              if stack[-1] == '{' and s == '}':
                  stack.pop()
                  continue
              if stack[-1] == '(' and s == ')':
                  stack.pop()
                  continue

            stack.append(s)
        if len(stack) == 0:
            answer += 1
        q.rotate(1)
        n -= 1
    # print(answer)
    return answer

# solution("[](){}")
# solution("}]()[{")
# solution("}]()[{") # 2
# solution("[)(]")
# solution("}}}")