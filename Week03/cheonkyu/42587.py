from collections import deque
def solution(priorities, location):
    answer = 0
    _p = [(i, val) for i, val in enumerate(priorities)]
    print(_p)
    queue = deque(_p)
    [i, max_p] = max(_p, key=lambda x: x[1])
    count = 0
    while queue:
        if queue[0][1] < max_p:
            queue.rotate(-1)
        else:
            do_process = queue.popleft()
            count += 1
            if queue:
              [_, max_p] = max(queue, key=lambda x: x[1])
            if do_process[0] == location:
                break

    answer = count
    # print(answer)
    return answer

# solution([2, 1, 3, 2], 2) # 1
# solution([1, 1, 9, 1, 1, 1], 0) # 5

# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5