from functools import reduce
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    answer = 0
    for i in range(row_begin - 1, row_end):
        print(data[i])
        tmp =reduce(lambda acc, cur: acc + (cur % (i + 1)), data[i], 0)
        print(tmp)
        answer ^= tmp
    print(answer)
    return answer

solution([[2],[1],[4],[3]],	1,	1,	4) # 4
# solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],	2,	1,	4) # 4
# solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],	2,	1,	4) # 4