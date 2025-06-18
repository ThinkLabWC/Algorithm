n = int(input())

names = [input() for i in range(n)]

dic = {}
for name in names:
  if not name[0] in dic:
    dic[name[0]] = 1
  else:
    dic[name[0]] = 1 + dic[name[0]]

result = []
for i, (k, v) in enumerate(dic.items()):
  if int(v) >= 5:
    result.append((k, v))

if len(result) == 0:
  print('PREDAJA')
else:
  result = sorted(result, key=lambda x: x[0])
  print(''.join(list(map(lambda x: x[0], result))))