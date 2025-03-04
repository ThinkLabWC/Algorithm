def solution(k, score):
    answer = []
    queue = []
    for s in score:
        print(queue)
        if len(queue) < k:
          queue.append(s)
        else:
          if min(queue) < s:
            i = queue.index(min(queue))
            del queue[i]
            queue.append(s)
        answer.append(min(queue))
    
    return answer

# solution(3, [10, 100, 20, 150, 1, 100, 200]) # [10, 10, 10, 20, 20, 100, 100]
