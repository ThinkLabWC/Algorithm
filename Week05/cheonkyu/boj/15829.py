n = int(input())
s = input()

result = 0
for i in range(0, len(s)):
  result += ((ord(s[i]) - ord('a') + 1) * (31 ** (i))) % 1234567891

print(result % 1234567891)