[a, b] = list(input().split(' '))

A = sum(list(map(int, list(a))))
B = sum(list(map(int, list(b))))
print(A * B)