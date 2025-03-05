def solution(numbers):
    total = sum(list(range(1,10)))
    target = sum(numbers)
    answer = total - target
    return answer