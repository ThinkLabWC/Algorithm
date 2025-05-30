from collections import Counter
n = int(input())
c = Counter(list(map(int, input().split())))
target = int(input())
print(c.get(target, 0))
