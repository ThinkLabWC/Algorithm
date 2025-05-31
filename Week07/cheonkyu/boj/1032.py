n = int(input())
data = [input() for i in range(n)]
result = ''
for i in range(0, len(data[0])):
  tmp = data[0][i]
  for j in range(1, n):
    if tmp != data[j][i]:
      tmp = '?'
      break
  result += tmp
print(result)