def to_str(n, base):
  converter = "0123456789ABCDEF"
  if n < base:
    return converter[n]
  else:
    return to_str(n // base, base) + converter[n % base]
  
def solution(n):
    answer = 0
    bin = to_str(n, 2)
    target = list(bin).count('1')
    next = n + 1
    while True:
        bin = to_str(next, 2)
        if target == list(bin).count('1'):
           answer = next
           break
        next += 1
    return answer

solution(78)