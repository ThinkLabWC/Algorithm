def isOk(n):
  s = list(str(n))
  for i in range(0, len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True


while True:
  n = int(input())
  if n == 0:
    break
  print('yes' if isOk(n) else 'no')