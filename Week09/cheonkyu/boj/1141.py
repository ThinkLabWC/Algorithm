N = int(input())
s = set()
tmp = [input() for _ in range(N)]
tmp = sorted(tmp, key=lambda x: len(x) * -1)
for a in tmp:
  if not s:
    s.add(a)
  else:
    ok = True
    for str in s:
      if str.find(a) == 0 or a.find(str) == 0:
        ok = False
        break
    if ok:
      s.add(a)
print(len(s))

