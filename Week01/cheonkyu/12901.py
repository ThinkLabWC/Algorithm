def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]

    total_day = b - 1
    for i in range(0, a - 1):
        total_day += month[i]
    answer = day[total_day % 7]
    return answer

print(solution(5, 24))