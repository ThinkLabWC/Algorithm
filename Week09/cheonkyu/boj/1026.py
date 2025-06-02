n = int(input())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(0, n):
  total += b[i] * a[i]
print(total)