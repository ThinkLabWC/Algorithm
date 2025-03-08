from functools import reduce

def solution(dartResult):
    answer = 0

    stack = []
    score = []
    score_dict = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    for d in dartResult:
        print(d, stack, score)
        if d in score_dict:
            # print(stack[-1])
            # print(score_dict[d])
            score.append(int(''.join(stack)) ** int(score_dict[d]))
            stack = []
        elif d == '*':
            if len(score) >= 1:
              score[-1] = score[-1] * 2
            if len(score) >= 2:
              score[-2] = score[-2] * 2
        elif d == '#':
            score[-1] = score[-1] * -1
        else:
          stack.append(d)
    answer = reduce(lambda x, y : x + y, score)
    return answer

# solution("1S2D*3T") # 37
# solution("1D2S#10S") # 9
# solution("1D2S0T") # 3
# solution("1S*2T*3S") # 23
# solution("1D#2S*3S") # 5
# solution("1T2D3D#") # -4
# solution("1D2S3T*") # 59
solution("0D") # 0
solution("2D") # 4
solution("10D*10T10T#") # 10
# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33