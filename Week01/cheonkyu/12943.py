def solution(num):
    if num == 1:
        return 0
    
    answer = 0
    while num != 1 and answer < 500:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer+=1
    if answer == 500:
        return -1
    return answer