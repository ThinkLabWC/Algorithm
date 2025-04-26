T = int(input())

def isPalendrom(s):
  for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True

for _ in range(0, T):
  n = int(input())
  data = [input() for __ in range(0, n)]
  ok = False
  out = "0"
  for i in range(0, len(data)):
    if ok:
      break
    for j in range(i + 1, len(data)):
      if isPalendrom(data[i] + data[j]):
        ok = True
        out = data[i] + data[j]
        break
      elif isPalendrom(data[j] + data[i]):
        ok = True
        out = data[j] + data[i]
        break
  print(out)
    