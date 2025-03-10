def to_bin(num):
    buffer = []
    while num > 0:
        if num % 2 == 0:
          buffer.append("0")
        else:
          buffer.append("1")
        num = int(num / 2)
    buffer.sort(reverse=True)
    result = ''.join(buffer)
    return result

def to_decimal(bin):
  size = len(bin)
  result = 0
  for i in range(0, size):
    result += int(bin[size-i-1]) * 2 ** i
  return result

def solution(s):
    answer = []
    n = 0
    zero_cnt = 0
    while s != '1':
      n += 1
      only_one = ''.join(s.split('0'))
      zero_cnt += len(s) - len(only_one)
      s = to_bin(len(only_one))
      
    answer = [n, zero_cnt] 
    # print(answer)
    return answer

# solution("110010101001")
# solution("01110")
solution("1111111")
# to_bin(16)