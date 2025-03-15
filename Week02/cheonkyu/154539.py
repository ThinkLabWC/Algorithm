def solution(numbers):
    answer = [0] * len(numbers)
    stack = [0]
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)
    # print(answer)
    # print(stack)
    
    while stack:
        answer[stack[-1]] = -1
        stack.pop()
    return answer

solution([2, 3, 3, 5]) # , [3, 5, 5, -1]