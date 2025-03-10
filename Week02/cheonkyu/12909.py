def solution(s):
    answer = True
    
    stack = []
    for i in range(len(s)):
        # print(stack)
        if stack:
            if stack[-1] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    answer = len(stack) == 0
    # print(answer)
    return answer

# solution("()()") # True
# solution("(())()") # True
# solution(")()(") # false
# solution("(()(") # false