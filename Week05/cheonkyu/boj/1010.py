from math import factorial

n = int(input())

data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

for item in data:
  a = int(item[0])
  b = int(item[1])
  anwer = factorial(b) // (factorial(b-a) * factorial(a))
  print(anwer)