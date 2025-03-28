def solution(n):
    answer = 0
    dp = [0 for i in range(max(n + 1, 6))] 
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    for i in range(5, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n]
    print(answer)
    return answer

# solution(4) # 5
solution(3) # 3
# 4	5
# 3	3
# 1 (1)
# 2 (1,1), (2)
# 3 (1,1,1), (2,1), (1,2)
# 4 (1,1,1,1), (2,1,1), (1,2,1), (1,1,2), (2,2)