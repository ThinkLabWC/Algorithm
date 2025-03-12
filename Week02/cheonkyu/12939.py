def solution(s):
    answer = ''
    a = list(map(lambda x: int(x), s.split(' ')))
    answer += str(min(a))
    answer += ' '
    answer += str(max(a))
    # print(answer)
    return answer

solution("1 2 3 4")