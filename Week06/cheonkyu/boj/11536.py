N = int(input())
data = [input() for _ in range(0, N)]
asc = sorted(data)
dsc =sorted(data, reverse=True)

asc_count = 0
dsc_count = 0
is_neither = False
for i in range(0, len(data)):
  if data[i] == asc[i]:
    asc_count += 1
  elif data[i] == dsc[i]:
    dsc_count += 1
  else:
    is_neither = True
    break
if is_neither:
  print("NEITHER")
elif asc_count > dsc_count:
  print("INCREASING")
else:
  print("DECREASING")
