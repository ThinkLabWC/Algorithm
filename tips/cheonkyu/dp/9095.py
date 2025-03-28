import sys
si = sys.stdin.readline

def solution(n):
  dp = [0] * 11
  dp[0] = 1
  dp[1] = 2
  dp[2] = 4
  for i in range(3, n):
    dp[i] = dp[i-2] + dp[i-1] + dp[i-3]
  print(dp[n - 1])
  
T = int(si())
for _ in range(T):
    solution(int(si()))