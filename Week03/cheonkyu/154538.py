def solution(x, y, n):
    answer = 0
    dp = [1e9] * (y+1)
    dp[x] = 0
    for i in range (x, y+1):
        if dp[i] == 1e9:
            continue
        if i + n <= y:
            dp[i+n] = min(dp[i+n], dp[i] + 1)
        if i * 2 <= y:
            dp[i*2] = min(dp[i*2], dp[i] + 1)
        if i * 3 <= y:
            dp[i*3] = min(dp[i*3],dp[i] + 1)
    
    if dp[y] == 1e9:
        return -1
    return dp[y]
# solution(10, 40, 5) # 2
# solution(10, 40, 30) # 1
solution(2, 5, 4) # -1
# x	y	n	result
# 10	40	5	2
# 10	40	30	1
# 2	5	4	-1