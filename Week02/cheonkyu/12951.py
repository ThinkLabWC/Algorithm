def solution(s):
    answer = ''
    s = s.lower()
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            uppered = word[0].upper()
            result.append(uppered + (word[1:] if len(word) >= 2 else ''))
        else:
            result.append(word)
    answer = ' '.join(result)
    return answer

# solution("3people unFollowed me")
# solution("3people   me")
solution(" 1 3people   me")
# solution()
# print("1"[0].upper())
