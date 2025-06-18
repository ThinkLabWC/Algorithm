a = [4,2,3,3,3,3,3,3,3,3]

while True:
  n = int(input())
  if n == 0:
    break
  result = len(str(n)) + 1
  for c in str(n):
    result += a[int(c)]
  print(result)