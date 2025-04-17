N, M = map(int, input().split())

p = {}
for i in range(1, N + 1):
  item = input()
  p[str(i)] = item
  p[item] = i

for i in range(0, M):
  answer = input()
  print(p[answer])