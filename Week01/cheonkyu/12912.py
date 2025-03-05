def solution(a, b):
    answer = 0
    small = b if a > b else a
    large = a if a >= b else b
    if small == large:
      return small
    for i in range(small, large + 1):
        answer += i
    return answer

solution(3, 5)
solution(5, 3)