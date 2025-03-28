def solution(n, a, b):
    answer = 0
    dp = [[] for i in range(0, n)]
    # print(n, a, b, dp)
    dp[0] = [(i + 1) for i in range(0, n)]
    # print(dp)
    l = n
    ok = False
    for i in range(1, len(dp)):
        if ok:
           break
        answer += 1
        # print(i, l)
        for j in range(0, l - 1, 2):
          print(i, j)
          if dp[i-1][j] == a and dp[i-1][j + 1] == b:
             ok = True
             break
          elif dp[i-1][j] == b and dp[i-1][j + 1] == a:
             ok = True
             break
          
          if dp[i-1][j] == a or dp[i-1][j + 1] == a:
            dp[i].append(a)
          elif dp[i-1][j] == b or dp[i-1][j + 1] == b:
            dp[i].append(b)
          else:      
            dp[i].append(dp[i-1][j])
        l = l // 2
    # print(dp, answer)
    return answer

# solution(8, 4, 7)
# solution(4, 1, 2)
# 8	4	7	3

# 1 2 3 4 5 6 7 8
# 1 4 5 7
# 4 7

# 1 2 3 4
# 