s = input()
# s = 'ljes=njak'
# s = 'ddz=z='
# s = 'nljj'
# s = 'c=c='
# s = 'dz=ak'
special_chars = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
i = 0
while i < len(s):
  if i < len(s) - 2 and s[i] + s[i+1] + s[i+2] in special_chars:
    i += 2
  elif i < len(s) - 1 and s[i] + s[i+1] in special_chars:
    i += 1
  count += 1
  i += 1

print(count)