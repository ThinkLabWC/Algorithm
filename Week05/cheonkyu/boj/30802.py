from math import ceil

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
res = sum([ceil(el / t) for el in size])

print(res)
print(sum(size) // p, sum(size) % p)