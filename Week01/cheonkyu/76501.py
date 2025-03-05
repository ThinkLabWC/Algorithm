def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(signs)):
        answer += absolutes[i] * (1 if signs[i] else -1)
    return answer