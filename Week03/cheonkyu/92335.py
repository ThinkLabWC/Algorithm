def to_str(n, base):
  converter = "0123456789ABCDEF"
  if n < base:
    return converter[n]
  else:
    return to_str(n // base, base) + converter[n % base]
  
def is_prime(n):
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def solution(n, k):
    answer = 0
    bin = to_str(int(n), k)
    print(bin)
    list = str(bin).split('0')
    dp = {}
    
    for a in list:
       if a == '1':
         continue
       if a in dp and dp[a]:
        answer += 1
       elif not a in dp and a != '':
        dp[a] = is_prime(int(a))
        if dp[a]:
          answer += 1
    # print(answer)
    return answer

# solution("437674", 3)
# solution("110011", 10)
# 110011	10	2