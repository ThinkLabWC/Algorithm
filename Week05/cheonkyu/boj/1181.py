N = int(input())

s = set()
for _ in range(0, N):
  s.add(input())

data = list(s)
data.sort(key= lambda x: (len(x), x))
for item in data:
  print(item)