def solution(n):
    a = list(str(n))
    a.sort(reverse=True)
    answer = int(''.join(a))
    return answer

# solution(12345)