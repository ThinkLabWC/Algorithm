
while True:
    try:
      [s, t] = input().split()
      i = 0
      for j in range(0, len(t)):
        if s[i] == t[j]:
          i += 1
        if i >= len(s):
          break
      if i == len(s):
        print('Yes')
      else:
        print('No')
      if s == '':
        break
    except:
        break
    


