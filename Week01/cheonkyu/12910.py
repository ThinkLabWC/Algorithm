def solution(arr, divisor):
    data = list(filter(lambda x: x % divisor == 0, arr))
    if not data:
        return [-1]
    data.sort()
    answer = data
    return answer