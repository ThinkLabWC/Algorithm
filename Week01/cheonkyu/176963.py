from functools import reduce
def getTotalYearning(nameByYearningDic, photo):
    score = reduce(lambda acc, cur: acc + nameByYearningDic.get(cur, 0), photo, 0)
    return score

def solution(name, yearning, photos):
    nameByYearningDic = dict(zip(name, yearning))

    answer = []
    for photo in photos:
        score = getTotalYearning(nameByYearningDic, photo)
        answer.append(score)
    
    return answer

# solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])