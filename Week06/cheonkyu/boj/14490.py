from sys import stdin
from math import gcd
[a, b] = stdin.readline().split(':')
g = (gcd(int(a), int(b)))
print(f"{int(a)//g}:{int(b)//g}")

