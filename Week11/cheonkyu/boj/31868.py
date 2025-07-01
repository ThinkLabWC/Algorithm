n, k = map(int, input().split())

result = 0
for i in range(0, n - 1):
  k = k // 2
  print(k)
result = k
print(result)