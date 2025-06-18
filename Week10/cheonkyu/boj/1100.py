chess = [input() for i in range(8)]

result = 0 
for i in range(len(chess)):
  for j in range(len(chess[0])):
    if i % 2 == 0 and j % 2 == 0 and chess[i][j] == 'F':
      result += 1
    elif i % 2 != 0 and j % 2 != 0 and chess[i][j] == 'F':
      result += 1
print(result)
