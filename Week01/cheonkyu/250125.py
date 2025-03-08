def solution(board, h, w):
    answer = 0

    cur = board[h][w]
    data_list = [(0,1),(-1,0),(1,0),(0,-1)]
    for data in data_list:
        x, y = data
        if (h + x) >= 0 and (w + y) >= 0 and (h + x) < len(board) and (w + y) < len(board):
            if cur == board[h + x][w + y]:
                answer += 1 
    # print(answer)
    return answer


solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],	1,	1) #	2
# solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],	0,	1) #	1