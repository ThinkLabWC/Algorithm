n = int(input())
strs = [input() for i in range(n)]
for s in strs:
  print(s[0] + s[-1])
