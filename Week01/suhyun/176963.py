def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    print(info)

    for people in photo:
        score = 0
        for person in people:
            score += info.get(person, 0)
        answer.append(score)
    return answer