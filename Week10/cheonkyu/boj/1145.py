from math import lcm
data = list(map(int, input().split(' ')))

result = lcm(data[0], data[1], data[2])
for i in range(len(data)):
  for j in range(i + 1, len(data)):
    for k in range(j + 1, len(data)):
      result = min(result, lcm(data[i], data[j], data[k]))
print(result)

  