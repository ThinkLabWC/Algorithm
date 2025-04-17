n = int(input())
answer = n // 5 + (0 if n % 5 == 0 else 1)
print(answer)