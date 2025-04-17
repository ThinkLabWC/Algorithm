n = int(input())
a = 3
b = 5

cnt = 0
while n > 0:
  cnt += 1
  if n % 5 == 0:
    n -= 5
  elif n % 3 == 0:
    n -= 3
  else:
    n -= 5

if n < 0:
  print(-1)
else:
  print(cnt)
