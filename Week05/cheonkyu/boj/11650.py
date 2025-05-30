N = int(input())

data = []
for _ in range(0, N):
  data.append(list(map(int, input().split(' '))))

data.sort(key=lambda x: (x[0], x[1]))
for item in data:
  print(f"{item[0]} {item[1]}")