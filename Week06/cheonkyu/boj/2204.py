
while True:
  n = int(input())
  if n == 0:
    break
  data = [input() for _ in range(n)]
  data.sort(key = lambda x: x.lower())
  print(data[0])
