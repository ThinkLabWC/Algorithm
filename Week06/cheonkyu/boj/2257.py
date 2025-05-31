s = input()

d = {
    "H" : 1,
    "C" : 12,
    "O" : 16
}

stack = []

for i in s:
    if i in d:
        stack.append(d[i])
    elif i == "(":
        stack.append(i)
    elif i == ")":
        temp = 0
        while True:
            p = stack.pop()

            if p == "(":
                break

            temp += p
        
        if temp == 0:
            continue
        else:
            stack.append(temp)
    else:
        n = stack.pop()
        temp = n*int(i)
        stack.append(temp)
