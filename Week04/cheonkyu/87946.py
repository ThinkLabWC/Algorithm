from itertools import permutations
def solution(k, dungeons):
    answer = -1
    data = [i for i in range(len(dungeons))]
    all = list(permutations(data, len(dungeons)))
    for row in all:
        p = k
        count = 0
        for i in list(row):
            [required, used] = dungeons[i]
            if p >= required:
                p -= used
                count += 1
            # print(dungeons[i])
        answer = max(answer, count)
    # print(answer)
    return answer
    

solution(80, [[80,20],[50,40],[30,10]])