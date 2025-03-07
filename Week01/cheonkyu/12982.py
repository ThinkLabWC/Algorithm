def solution(d, budget):
    answer = 0
    d.sort()
    total = 0
    for price in d:
        if (total + price) <= budget:
            total += price
            answer += 1
        else:
            break
    return answer

solution([1,3,2,5,4], 9)

solution([2,2,3,3,], 9)