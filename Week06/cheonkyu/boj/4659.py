
data = []
while True:
  s = input()
  if s == 'end':
    break
  data.append(s)

def step1(s):
  for c in ['a', 'e', 'i', 'o', 'u']:
    if c in s:
      return True
  else:
    return False
  
def step2(s):
  m = ['a', 'e', 'i', 'o', 'u']
  for i in range(0, len(s) - 2):
    if s[i] in m and s[i + 1] in m and s[i + 2] in m:
      return False
    elif not s[i] in m and not s[i + 1] in m and not s[i + 2] in m:
      return False
  return True

def step3(s):
  for i in range(0, len(s) - 1):
    if s[i] == s[i + 1] and s[i] != 'e' and s[i] != 'o':
      return False
  return True

for item in data:
  ok = True
  ok = step1(item)
  if ok:
    ok = step2(item)
  if ok:
    ok = step3(item)
  if ok:
    print(f"<{item}> is acceptable.")
  else:
    print(f"<{item}> is not acceptable.")
