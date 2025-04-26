s = input()
case = []
ucpc = ['U', 'C', 'P', 'C']
for i in range(0, len(s)):
  if s[i] in ucpc:
    case.append(s[i])

id = 0
for i in range(0, len(case)):
  if id >= 4:
    break
  if case[i] == ucpc[id]:
    id += 1

if id >= 4:
  print('I love UCPC')
else:
  print('I hate UCPC')