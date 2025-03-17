from collections import Counter
def solution(s):
    a = s[2:-2]
    a = a.split('},{')
    a = [i.split(',') for i in a]
    a.sort(key=lambda x: len(x))
    answer = a[0]
    for i in range(1, len(a)):
        n_dict = Counter(answer)
        for j in range(len(a[i])):
            n_dict[a[i][j]] -= 1
        for key, val in n_dict.items():
            if val == -1:
                answer.append(key)
    
    answer = list(map(lambda x: int(x), answer))
    # print(answer)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
# solution("{{20,111},{111}}") # [111, 20]
# solution("{{123}}") # [123]
# solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") # [3, 2, 4, 1]
