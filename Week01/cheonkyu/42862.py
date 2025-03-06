def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _lost = list(filter(lambda x: not x in reserve, lost))
    _reserve = list(filter(lambda x: not x in lost, reserve))
    answer = n - len(_lost)
    for r in _reserve:
        if (r - 1) in _lost:
            _lost.pop(_lost.index(r - 1))
            answer += 1
        elif (r + 1) in _lost:
            _lost.pop(_lost.index(r + 1))
            answer += 1
    print(answer)
    return answer


# solution(5, [2, 4], [1, 3, 5])
# solution(5, [2, 4], [3])
# solution(3, [3], [1])
# solution(10, [6,8,9], [4,7])
# solution(3, [3], [3])

# solution(5, [4, 2], [3, 5]) # 5
solution(5, [5, 3], [4, 2]) # 5

