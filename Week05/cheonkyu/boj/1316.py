N = int(input())

data = []
for i in range(0, N):
  data.append(input())

def isGroup(s):
  d = {}
  for i in range(0, len(s)):
    ch = s[i] 
    if not ch in d:
      d[ch] = True
    else:
      if s[i - 1] == s[i]:
        continue
      return False
  return True

count = 0
for item in data:
  if isGroup(item):
    count += 1

print(count)