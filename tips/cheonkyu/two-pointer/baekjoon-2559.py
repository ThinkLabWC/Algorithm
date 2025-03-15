def solution(temps, n):
  tmp = sum(temps[0:n])
  answer = tmp
  for i in range(1, len(temps) - n + 1):
    # print( temps[i + n])
    tmp = tmp - temps[i-1] + temps[i + n - 1]
    answer = max(tmp, answer)
    print(tmp)
  print(answer)


solution([3, -2, -4, -9, 0, 3, 7, 13, 8, -3], 10)