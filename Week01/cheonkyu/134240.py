def solution(food):
    answer = ''
    food.pop(0)
    queue = []
    for i in range(0, len(food)):
        if int(food[i] / 2) >= 1:
          for j in range(0, int(food[i] / 2)):
             queue.append(str(i + 1))
    answer += ''.join(queue)
    queue.reverse()
    answer += '0'
    answer += ''.join(queue)
    return answer

# solution([1, 3, 4, 6]) #	"1223330333221"
# solution([1, 7, 1, 2]) #	"111303111"