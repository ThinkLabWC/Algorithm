def solution(n):
    answer = 1
    for i in range(1, n + 1):
        sum = 0
        for j in range(i + 1, n + 1):
            sum += j
            if sum == n:
                answer += 1
            if sum > n:
                break
    print(answer)
    return answer


solution(15)