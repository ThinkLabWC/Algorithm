def solution(prices):
    answer = []
    # print(prices)
    for L in range(len(prices)):
        times = 0
        for R in range(L + 1, len(prices)):
            times += 1
            if prices[L] > prices[R]:
                break
        answer.append(times)
    return answer

solution([1, 2, 3, 2, 3]) # [4, 3, 1, 1, 0]