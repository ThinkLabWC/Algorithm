def solution(a, b, n):
    answer = 0
    total = n
    while total >= a:
      # print('total = a * (total/a) + 나머지')
      # print(total, '=', a, '*', int(total/a), '+', total % a)
      diff = 0
      if total >= a:
         diff = total % a
      total = int(int(total / a) * b) + diff
      answer += total - diff

    return answer

# 20 / 2 = 10
# 10 / 2 = 5
# 5 / 2 = 4 + 1
# 5 / 2 = 2 + 1
# 2 / 2 = 1

# 20 = 3 * 6 + 2
# 8 = 3 * 2 + 2
# 4 = 3 * 1 + 1
# solution(2, 1, 20) # 19
# solution(3, 1, 20) # 9
