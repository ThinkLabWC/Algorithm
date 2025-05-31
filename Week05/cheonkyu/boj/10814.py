N = int(input())

data = []
for _ in range(0, N):
  data.append(input().split())

data.sort(key = lambda x: int(x[0]))
# print(data)
for item in data:
  print(f"{item[0]} {item[1]}")