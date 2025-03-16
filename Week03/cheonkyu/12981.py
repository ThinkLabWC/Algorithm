def solution(n, words):
    answer = [0, 0]
    s = set()
    turn = 0
    who = 0
    out = False
    for i in range(len(words)):
        who = i % n + 1
        word = words[i]
        # print(i - 1 >= 0)
        if i - 1 >= 0 and word[0] != words[i - 1][-1]:
            out = True
            turn = i
            # print(i, n, words[i])
            break
        if word in s:
            turn = i
            out = True
            break
        else:
            s.add(word)

    if not out:
         return [0, 0]
    answer = [who, int(turn / n) + 1]

    return answer


# solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) # [3,3]
# solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
# solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) #	[1,3]
# solution(2, ["hello", "ane"]) #	[1,3]