def solution(k, tangerine):
    answer = 0
    t_dict = {}
    for t in tangerine:
        t_dict[t] = t_dict[t] + 1 if t in t_dict else 1
    b = dict(sorted(t_dict.items(), key=lambda item: -item[1]))
    total = 0
    # print(b)
    for key,val in b.items():
        if total < k:
            answer += 1
            total = total + val
        else:
            break
    return answer

# solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) # 3
# solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) # 2
solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) # 1

# a = [1, 3, 2, 5, 4, 5, 2, 3]
# a.sort()
# print(a)