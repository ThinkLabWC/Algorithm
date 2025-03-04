def findKey(keymaps, char):
    result = 9999
    for keymap in keymaps:
        i = (keymap.index(char) if char in keymap else 9999) + 1
        result = min([i, result])
        
    return result
    
def solution(keymaps, targets):
    answer = []
    charDic = {}
    for target in targets:
        count = 0
        for i in range(0, len(target)):
            char = target[i]
            if charDic.get(char) == None:
              step = findKey(keymaps, char)
              charDic[char] = step
            count += charDic[char]
        answer.append(count)
    answer = list(map(lambda x: -1 if x >= 9999 else x, answer))
    return answer

# solution(["ABACD", "BCEFD"], ["ABCD","AABB"]) # [9, 4]
# solution(["AA"], ["B"]) # [-1]
# solution(["AGZ", "BSSS"], ["ASA","BGZ"]) # [4, 6]