def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)

    box = score
    for i in range(0, len(score), m):
        box = score[i:i + m]
        if len(box) < m:
            break
        print(score[i:i + m])
        price = min(score[i:i + m])
        answer += price * m
    # print(answer)
    return answer


# solution(3, 4, [1,2,3,1,2,3,1]) # 8
# solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2]) # 33