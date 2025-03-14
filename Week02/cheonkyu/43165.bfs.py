# BFS를 이용한 풀이
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
            print(tmp)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

# 1 + 1 + 1 + 1 + 1 = 5
solution([1, 1, 1, 1, 1], 3) # 5
# solution([4, 1, 2, 1], 4) # 2