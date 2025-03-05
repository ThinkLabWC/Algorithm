def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(0, count):
        total += price * (i + 1)
    answer = total - money
    return answer if answer >= 0 else 0

# a = solution(3, 20, 4)
a = solution(2, 4, 1)
print(a)