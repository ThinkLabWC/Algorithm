def solution(progresses, speeds):
    answer = []
    
    while True and progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        
        task = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            task += 1
        if task > 0:
            answer.append(task)
    # print(answer)
    return answer

# solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])

# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]