def check_score(choices, answers):
    result = 0
    size = len(choices)
    for i in range(0, len(answers)):
        if answers[i] == choices[i % size]:
            result += 1
    return result

def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    a1 = check_score(a, answers)
    b1 = check_score(b, answers)
    c1 = check_score(c, answers)
    user = [a1, b1, c1]
    max_score = max(user)
    for i in range(0, len(user)):
        if user[i] == max_score:
            answer.append(i + 1)
            
    return answer

solution([1, 2, 3, 4, 5]) # [1]
# solution([1, 3, 2, 4, 2]) # [1, 2, 3]