def solution(secret, skip, index):
    answer = ''
    char = []
    for i in range(ord('a'), ord('z')+1):
        if not chr(i) in skip:
            char.append(chr(i))
    for s in secret:
        i = (char.index(s) + index) % len(char)
        answer += char[i]
    return answer

# answer = solution("aukks", "wbqd", 5) # "happy"
# # "aukks"	"wbqd"	5	"happy"
# print(answer)