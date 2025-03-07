def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        print('move', move)
        for i in range(0, len(board)):
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 1

            if board[i][move - 1] != 0:
                stack.append(board[i][move - 1])
                print('stack', stack)
                board[i][move - 1] = 0
                break
            
    return answer * 2


# solution(
#     [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
#     [1,5,3,5,1,2,1,4]
# )
