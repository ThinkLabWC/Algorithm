from itertools import permutations
import math
num = input()
# num = '27711'
data = list(map(lambda x: int(''.join(x)), (permutations(list(num), len(num)))))

result = math.inf
for item in data:
  if (item > int(num)):
    result = min(item, result)
if math.inf == result: 
  result = 0
print(result)

