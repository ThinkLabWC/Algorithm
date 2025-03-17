def solution(numbers):
    answer = ''
    strs = list(map(lambda x: str(x), numbers))
    strs.sort(reverse=True, key= lambda x: x * 3)
    # print(strs)
    answer = ''.join(strs)
    # print(strs)
    return answer if len(answer)!= answer.count('0') else '0'
# 9534303
# 9534330
# solution([3, 30, 34, 5, 9])
# solution([6, 10, 2])
solution([1, 2, 3, 4, 40, 41])
