import sys
input = sys.stdin.readline
n = int(input())
s = [input().split() for i in range(n)]

result = sorted(s, key = lambda x: (int(x[1]), int(x[0])))
for row in result:
  print(row[0] + ' ' + row[1])