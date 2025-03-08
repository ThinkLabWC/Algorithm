def diff_datetime(a, b):
    [y, m, d]= list(map(lambda x: int(x), a.split('.')))
    [y1, m1, d1]= list(map(lambda x: int(x), b.split('.')))
    total_m = 0
    total_m += (y - y1) * 12
    total_m += (m - m1)
    if d - d1 < 0:
        total_m = total_m - 1
    return total_m

def solution(today, terms, privacies):
    answer = []

    term_dict = {}
    for term in terms:
        [id, limit] = term.split(' ')
        term_dict[id] = int(limit)
    for i in range(0, len(privacies)):
        p = privacies[i]
        [date, id] = p.split(' ')
        m = diff_datetime(today, date)
        print(m)
        if term_dict[id] <= m:
            answer.append(i + 1)

    # print(answer)
    return answer

# solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]) # [1, 3]
# solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]) # [1, 4, 5]