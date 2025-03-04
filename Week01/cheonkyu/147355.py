def solution(t, p):
    answer = 0
    queue = []
    for i in range(0, len(t)):
        size = len(p)
        if size + i < len(t):
          queue.append(t[i:size + i])
    answer = list(filter(lambda x: x <= p, queue))
    return answer

solution("3141592", "271")
# solution("500220839878", "7")
# solution("10203", "15")

# "3141592"	"271"	2
# "500220839878"	"7"	8
# "10203"	"15"	3