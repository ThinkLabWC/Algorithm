def get_decimal_list(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def solution(n):
    d = get_decimal_list(n)
    print(d)
    answer = sum(d)
    return answer