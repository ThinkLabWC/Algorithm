a = input()
b = input()

i = 0
answer = 0
while i < len(a):
  if a[i:i + len(b)] == b:
    i += len(b)
    answer += 1
  else:
    i += 1

print(answer)

