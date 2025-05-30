N = int(input())

data = []
for i in range(0, N):
  data.append(list(map(int, input().split(' '))))

result = []
for i in range(0, len(data)):
  rank = 0
  for j in range(0, len(data)):
    if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
      rank += 1
  result.append(rank)
rank = list(map(lambda x: x + 1, result))
for r in rank:
  print(r)