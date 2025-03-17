import copy

def check_str(str):
    for s in str:
        if ord('A') <= ord(s) and ord(s) <= ord('Z'):
            pass
        else:
            return False
    return True

def solution(str1, str2):
    answer = 0

    s1 = [(str1[i] + str1[i + 1]).upper() for i in range(len(str1) - 1)]
    s2 = [(str2[i] + str2[i + 1]).upper() for i in range(len(str2) - 1)]
    
    s1 = list(filter(lambda x: check_str(x), s1))
    s2 = list(filter(lambda x: check_str(x), s2))
    org_s2 = copy.deepcopy(s2)
    print(s1)
    print(s2)
    print('---')
    intract_set = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                s2[j] = '-'
                intract_set.append(s1[i])
                break
    s2 = org_s2
    union_set = copy.deepcopy(intract_set)
    tmp1 = copy.deepcopy(intract_set)
    tmp2 = copy.deepcopy(intract_set)

    for i in range(len(s1)):
        # print(s1[i], tmp1)
        if s1[i] in tmp1:
            tmp1.pop(tmp1.index(s1[i]))
        else:
            print(s1[i])
            union_set.append(s1[i])
    for i in range(len(s2)):
        if s2[i] in tmp2:
            tmp2.pop(tmp2.index(s2[i]))
        else:
            union_set.append(s2[i])

    # print(intract_set)
    # print(union_set)
    if len(intract_set) == 0 and len(union_set) == 0:
        return 65536
    answer = int((len(intract_set) / len(union_set)) * 65536)
    # print(answer)
    return answer

# solution("FRANCE", "french") # 16384
# solution("handshake", "shake hands") # 65536
# solution("aa1+aa2", "AAAA12") # 43690
# solution("E=M*C^2", "e=m*c^2") # 65536
# solution("ABABAB", "BABABA") # 43690

# ['AB', 'BA', 'AB', 'BA', 'AB']
# ['BA', 'AB', 'BA', 'AB', 'BA']