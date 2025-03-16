def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    answer = dp[-1] 
    # print(answer)
    return answer

solution(2)
# solution(4)
# n = 2 # 2
# n = 3 # 2 + 1
# n = 4 # 5
# n = 5 # 8