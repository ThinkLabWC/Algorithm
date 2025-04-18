# data = 'abab'
# data = 'qwerty'
# data = 'abdfhdyrbdbsdfghjkllkjhgfds'
# abdfhdyrbdb
# data = 'abdfhdyrbdbsdfghjkllkjhgfds'
# data = 'abacaba'
data = input()

def isOk(data):
  if len(data) == 1:
    return False
  for i in range(0, int(len(data) / 2) + 1):
    if data[i] != data[len(data) - i - 1]:
      return False
  return True

def solution(data):
  end = len(data) - 1
  for i in range(0, len(data) - 1):
    ok = isOk(data[-(len(data) - i):])
    if ok:
      end = i
      break
  
  stub = ''
  for i in range(0, end):
    stub += data[end - i - 1]
  result = data + stub
  print(len(result))
  # print(end)

solution(data)