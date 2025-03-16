def solution(s):
    answer = -1
    
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    answer = 1 if len(stack) == 0 else 0
    # print(answer)
    return answer

solution("baabaa") # 1
solution("cdcd") # 1