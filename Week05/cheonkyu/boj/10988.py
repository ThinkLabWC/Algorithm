str = input()
ok = True
for i in range(0, int(len(str) // 2)):
  if str[i] != str[len(str) - i - 1]:
    ok = False
    break
print(1 if ok else 0)