data = []
while True:
  item = list(map(int, input().split(' ')))
  if item[0] == 0:
    break
  data.append(item)

for item in data:
  item = sorted(item)
  if item[0] ** 2 + item[1] ** 2 == item[2] ** 2:
    print('right')
  else:
    print('wrong')