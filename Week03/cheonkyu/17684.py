def solution(msg):
    answer = []
    c_dict = dict(zip([chr(i) for i in range(ord('A'), ord('Z') + 1)], list(range(1, ord('Z') - ord('A') + 2))))
    data = list(msg)
    top = 26
    i = 0
    while i < len(data):
        id = 0
        # print(c_dict)
        key = ''
        hit_key = ''
        for j in range(i + 1, len(data) + 1):
            key = ''.join(data[i:j])
            # print('a' ,i, key)
            if key in c_dict:
                hit_key = key
                id = max(c_dict[key], id)
                # print(i, 'hit', key, id)
            else:
                break
                # print('new', key)
                # break
        # print(key, id, len(key))
        answer.append(id)
        if not key in c_dict:
            top += 1
            c_dict[key] = top
        
        i = i + len(hit_key)
    # print(answer)
    return answer

# solution("KAKAO") #	[11, 1, 27, 15]
# solution("TOBEORNOTTOBEORTOBEORNOT") # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
solution("ABABABABABABABAB") #  [1, 2, 27, 29, 28, 31, 30]
