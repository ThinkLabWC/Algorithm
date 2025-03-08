def solution(participant, completion):
    completion_dict = dict(zip(completion, [0]*len(completion)))
    # completion_dict = {}
    for c in completion:
        completion_dict[c] += 1
    for p in participant:
        if p in completion_dict:
            completion_dict[p] = completion_dict[p] - 1
        else:
            completion_dict[p] = -1
    for key, val in completion_dict.items():
        if val == -1:
            return key
    return ""

# a = solution(
#     ["mislav", "stanko", "mislav", "ana"],
#     ["stanko", "ana", "mislav"]
# )
# print(a)

a = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(a)