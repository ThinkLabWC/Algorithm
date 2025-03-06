def isDecimal(n):
    if n == 1:
        return False
    for i in range(2, int(n **(1/2)) + 1):
        if n != i and n % i == 0:
            return False
    return True

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if isDecimal(i):
            answer += 1
    # print(answer)
    return answer

solution(10) # 4
solution(5) # 3
