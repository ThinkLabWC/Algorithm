def solution(s):
    answer = []
    dic = {}
    for i in range(0, len(s)):
        if dic.get(s[i]) == None:
            dic[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i
    return answer

# solution("banana") # 	[-1, -1, -1, 2, 2, 2]
# solution("foobar") # [-1, -1, 1, -1, -1, -1]