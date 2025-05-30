from collections import Counter

# data = [('WWBB', 'BBWB')]
# # data = [('BBBBBBB', 'BWBWBWB')]
# # data = [('WBBWW', 'WBWBW')]


# 'WBBWW'
# 'WBWBW'
# 'W' : 3, 'B': 2
# 'W' 'W' | 'W' : 2, 'B': 2
# 'B' 'B' | 'W' : 2, 'B': 1
# 'B' 'W' | 'W' : 1, 'B': 1
# 'W' 'B' | 'W' : 1, 'B': 0
# 'W' 'W' | 'W' : 0, 'B': 0

T = int(input())
data = []
for _ in range(0, T):
  N = int(input())
  prev = input()
  next = input()
  data.append((prev, next))

for item in data:
  a, b = item
  ac = Counter(list(a))
  tc = { 'W': 0, "B": 0 }
  count = 0
  for i in range(0, len(a)):
    if a[i] != b[i]:
      tc[b[i]] += 1
  count = max(tc['W'], tc['B'])
  print(count)