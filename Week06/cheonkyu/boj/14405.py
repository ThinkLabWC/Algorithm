s = input()
p = ["pi", "ka", "chu"]

i = 0
ok = True
while i < len(s):
  if i + 2 < len(s):
    if s[i:i+3] == 'chu':
      i += 3
      continue
  
  if i + 1 < len(s):
    if s[i:i+2] == 'pi' or s[i:i+2] == 'ka':
      i += 2
    else:
      ok = False
      break
  else:
    ok = False
    break
if not ok:
  print("NO")
else:
  print("YES")

