from functools import reduce
[n, m] = input().split()

data = [input().split() for _ in range(0, int(n))]
def handler(acc, cur):
  acc[cur[0]] = cur[1]
  return acc 
site_password = reduce(handler, data, {})

for i in range(0, int(m)):
  site = input()
  password = site_password.get(site)
  print(password)

