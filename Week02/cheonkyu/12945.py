def solution(n):
    answer = 0

    f = [0] * n
    f[0] = 1
    f[1] = 1
    for i in range(2, n):
        f[i] = (f[i-1] + f[i-2]) % 1234567
    answer = f[-1] % 1234567
    return answer

# solution(3) # 2
# solution(5) # 5