def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        d, m = divmod(yellow, i)
        if m != 0:
            continue
        # print(d * 2 + 4, i * 2)
        if (d * 2 + 4) + (i * 2) == brown:
            answer = [d + 2, i + 2]
            break
    # print(answer)
    return answer

solution(24,	24)