M, N = list(map(int, input().split()))

d = {
  1: 'One',
  2: 'Two',
  3: 'Three',
  4: 'Four',
  5: 'Five',
  6: 'Six',
  7: 'Seven',
  8: 'Eight',
  9: 'Nine',
  0: 'Zero',
}
d2 = {
  'One': '1',
  'Two': '2',
  'Three': '3',
  'Four': '4',
  'Five': '5',
  'Six': '6',
  'Seven': '7',
  'Eight': '8',
  'Nine': '9',
  'Zero': '0'
}

tmp = []
for i in range(M, N + 1):
  to_str = ' '.join(map(lambda x: d.get(int(x)), list(str(i))))
  tmp.append(to_str)

tmp.sort()

result = []
for num_str in tmp:
  to_num = ''.join(map(lambda x: d2.get(x), num_str.split(' ')))
  result.append(int(to_num))

for i in range(0, len(result)):
  print(result[i], end='')
  if i != len(result) - 1:
    print(' ', end='')
  if (i + 1) % 10 == 0:
    print('')