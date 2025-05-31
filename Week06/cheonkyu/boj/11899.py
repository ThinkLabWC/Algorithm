s = input()

stack = []
for i in range(len(s)):
  if not stack:
    stack.append(s[i])
  elif stack[-1] == '(' and s[i] == ')':
    stack.pop()
  else:
    stack.append(s[i])

print(len(stack))