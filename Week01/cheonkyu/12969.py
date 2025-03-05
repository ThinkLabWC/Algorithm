a, b = map(int, input().strip().split(' '))

s = ""
for i in range(0, b):
    for j in range(0, a):
        s += "*"
    s += "\n"
print(s)