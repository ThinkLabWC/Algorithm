import sys

dict_info = {}
count = 0 

words = []
while (1) :
    word = sys.stdin.readline().rstrip()
    if '-' in word:
        break
    words.append(word)

def solution(data):
  stack = []
  for i in range(0, len(data)):
    if stack and stack[-1] == '{' and data[i] == '}':
      stack.pop()
    else:
      stack.append(data[i])
  result = []
  cnt = 0
  for i in range(0, len(stack)):
    if i % 2 == 0 and stack[i] == '}':
      cnt += 1
      result.append('{')
    elif i % 2 != 0 and stack[i] == '{':
      cnt += 1
      result.append('}')
    else:
      result.append(stack[i])
  # print(result, cnt)
  return cnt

for i in range(0, len(words)):
  word = words[i]
  cnt = solution(word)
  print(f"{i + 1}. {cnt}")
