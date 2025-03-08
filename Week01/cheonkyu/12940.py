def solution(n, m):
    answer = []
    a = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            a = i
    b = n * int(m / a)
    return answer

solution(3, 12)
solution(2, 5)