def is_good(numbers, i):
  L = 0
  R = len(numbers) - 1
  target = numbers[i]
  while L < R:
    if L == i:
      L += 1
    elif R == i:
      R -= 1
    else:
      if numbers[L] + numbers[R] > target:
        R -= 1
      elif  numbers[L] + numbers[R] < target:
        L += 1
      else:
        return True
  return False

def solution(numbers):
  answer = 0
  numbers.sort()
  for i in range(len(numbers)):
    if is_good(numbers, i):
      answer += 1
  print(answer)

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
