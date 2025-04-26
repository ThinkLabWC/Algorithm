[N, M] = input().split()

ns = set([input() for i in range(0, int(N))])
ms = set([input() for i in range(0, int(M))])

result = sorted(list(ns & ms))
print(len(result))
for name in result:
  print(name)
