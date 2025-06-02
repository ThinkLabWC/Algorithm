import sys
input = sys.stdin.readline

def char_counter(str):
  a = ['a', 'e', 'i', 'o', 'u']
  result = 0
  for c in str:
    if c.lower() in a:
      result += 1
  return result

while True:
  s = input()
  if s == '#\n':
    break
  count = char_counter(s)
  print(count)

