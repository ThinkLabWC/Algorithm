import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split(' ')))
tmp = list(set(nums))
result = sorted(tmp, key = lambda x: int(x))
print(' '.join(map(str, result)))