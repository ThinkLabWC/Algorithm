def solution(sequence, k):
    answer = [0, len(sequence)]
    r = 0
    sum = sequence[0]
    for l in range(len(sequence)):
        # print(l, r, sum)
        while r + 1 < len(sequence) and sum < k:
            r += 1
            sum += sequence[r]
        if sum == k:
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
        sum -= sequence[l]
    print(answer)
    return answer

# solution([1, 2, 3, 4, 5], 7) # [2, 3]
# solution([1, 1, 1, 2, 3, 4, 5],	5) #	[6, 6]
# [2, 2, 2, 2, 2]	6	[0, 2]
# solution([2,2,2,2,2], 6)
solution([4,2,7,6,2], 6)
