from collections import deque
target = input()
N = int(input())
data = []
for i in range(0, N):
  data.append(input())

result = 0
for item in data:
  if target in item:
    result += 1
  else:
    d = deque(item)
    d.rotate(1)
    while d != deque(item):
      if target in ''.join(d):
        result +=1
        break
      else:
        d.rotate(1)
print(result)