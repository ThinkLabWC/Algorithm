def solution(money, costs):
    unit = [1, 5, 10, 50, 100, 500]
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for j in range(len(unit)):
            coin = unit[j]
            cost = costs[j]
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + cost)

    # print(dp[money])
    print(dp[money])
    return dp[money]

# solution(4578, [1, 4, 99, 35, 50, 1000]) # 2308
solution(1999, [2, 11, 20, 100, 200, 600]) # 2798
# solution(100, [2, 2, 2, 2, 5, 9]) # 2798
