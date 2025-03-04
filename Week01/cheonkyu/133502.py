# 빵 – 야채 – 고기 - 빵
# 빵 1
# 야채 2
# 고기 3
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if ''.join(map(lambda x: str(x), stack[-4:])) == ''.join(['1','2','3','1']):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer+=1
    return answer


# solution([2, 1, 1, 2, 3, 1, 2, 3, 1]) # 2
solution([1, 3, 2, 1, 2, 1, 3, 1, 2]) # 0