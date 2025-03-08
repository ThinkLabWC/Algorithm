def get_distance(a, b):
    # return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = ''
    pos = {
        "L": "*",
        "R": "#"
    }
    metric_dict = {
       1: (0,0),
       2: (0,1),
       3: (0,2),
       4: (1,0),
       5: (1,1),
       6: (1,2),
       7: (2,0),
       8: (2,1),
       9: (2,2),
       "*": (3,0),
       0: (3,1),
       "#": (3,2),
    }
    phone = [
      [1,2,3],
      [4,5,6],
      [7,8,9],
      ["*", 0, "#"]
    ]
    # metrics = [
    #   [(0,0),(1,0),(2,0)],
    #   [(0,1),(1,1),(2,1)],
    #   [(0,2),(1,2),(2,2)],
    #   [(0,3),(1,3),(2,3)],
    # ]
    left = [1,4,7, "*"]
    right = [3,6,9, "#"]
    middle = [2,5,8,0]
    for n in numbers:
        if n in left:
            pos["L"] = n
            answer += 'L'
        if n in right:
            pos["R"] = n
            answer += 'R'
        if n in middle:
            for i in range(0, len(phone)):
                if n in phone[i]:
                    j = phone[i].index(n)
                    # print(i, j, phone[i][j])
                    target = (i, j)
                    left_pos = (0, 0)
                    right_pos = (0, 0)

                    left_pos = metric_dict.get(pos['L'])
                    right_pos = metric_dict.get(pos['R'])
                    l = get_distance(target, left_pos)
                    r = get_distance(target, right_pos)
                    # print('distance L', pos['L'],  left_pos, pos['R'], right_pos)
                    # print('distance', pos['L'],  left_pos, pos['R'], right_pos)
                    if l == r:
                        if hand == 'left':
                            pos["L"] = n
                            answer += 'L'
                        else:
                            pos["R"] = n
                            answer += 'R'
                    elif l > r:
                        pos["R"] = n
                        answer += 'R'
                    elif l < r:
                        pos["L"] = n
                        answer += 'L'
        # print('number', n, pos, answer)
    print(answer)
    return answer

# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") # "LRLLLRLLRRL"
# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	'left') # "LRLLRRLLLRR"
# solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right") # "LLRLLRLLRL"
solution([5, 1],	"right") # "RL"
solution([5, 1],	"left") # "LL"
solution([3, 1, 8],	"left") # "RLL"
solution([3, 1, 8],	"left") # "RLL"
solution([3, 1, 2, 4],	"left") # "RLLL"
solution([3, 1, 0],	"left") # "RLL"
solution([0,2,8,5],	"left") # "LLRL"
solution([0,2,8,5],	"right") # "RRLR"
solution([0,2,8,5],	"left") # "LLRL"
solution([0,2,8,5],	"right") # "RRLR"
solution([1,9],	"right") # "LR"
solution([2,9],	"right") # "RR"
solution([6,8],	"left") # "RL"
solution([0, 0], "right") # "RR"
solution([1, 1], "right") # "LL"
solution([8, 6], "left") # "LL"