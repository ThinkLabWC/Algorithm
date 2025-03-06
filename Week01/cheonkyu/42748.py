def solution(array, commands):
    answer = []
    for command in commands:
      [s, e, i] = command
      choice = array[s-1:e]
      choice.sort()
      answer.append(choice[i - 1])
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])  # [5, 6, 3] 