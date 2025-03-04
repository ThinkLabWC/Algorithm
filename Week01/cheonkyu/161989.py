def solution(n, m, section):
    answer = 0
    buffer = []
    for s in section:
        if not buffer:
          buffer.append(s)
        else:
          if m + buffer[-1] > s:
             continue
          else:
             buffer.append(s)
    answer = len(buffer)
    return answer


# solution(8,	4,	[2, 3, 6]) # 2
# solution(5,	4,	[1, 3]) #	1
# solution(4,	1,	[1, 2, 3, 4])	# 4