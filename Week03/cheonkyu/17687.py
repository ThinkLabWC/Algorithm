def to_str(n, base):
    converter = "0123456789ABCDEF"
    if n == 0 or base == 0:
       return 0
    if n < base:
      return converter[n]
    else:
      return to_str(n // base, base) + converter[n % base]

def solution(n, t, m, p):
    answer = ''

    i = 0
    all = ''
    while len(all) <= t * m:
       s = to_str(i, n)
       i += 1
       all += str(s)
    for i in range(len(all)):
        if len(answer) >= t:
           break
        if i % m == p - 1:
           answer += all[i]
    return answer

# solution(2, 4, 2, 1) # "0111"
# solution(10, 10, 2, 1) # "0111"
# solution(16, 16, 2, 1) # "02468ACE11111111"
# solution(16, 16, 2, 2) # "13579BDF01234567"


# 012345678910111213141516171819202122

# 036912
# 147111
# 258013