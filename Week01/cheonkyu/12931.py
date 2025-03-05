def solution(n):
    answer = 0
    num_list = list(str(n))
    for num in num_list:
        answer += int(num)

    return answer