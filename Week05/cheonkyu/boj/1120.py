# giorgi igroig
import math
# a = 'giorgi'
# b = 'igroig'
a, b = input().split(' ')

def check_diff(a, b):
  count = 0
  for i in range(0, len(a)):
    if a[i] != b[i]:
      count += 1
  return count

def solution(a, b):
  if len(a) < len(b):
    tmp = a
    a = b
    b = tmp
  count = math.inf
  if len(a) == len(b):
    count = check_diff(a, b)
  else:
    for i in range(0, len(a)):
      if len(a[i:len(b) + i]) == len(b):
        count = min(count, check_diff(a[i:len(b) + i], b))
        if count == 0:
          break
      else:
        break
  print(count)

solution(a,b)

# adaabc aababbc