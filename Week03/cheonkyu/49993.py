def solution(skill, skill_trees):
    answer = 0
    s = list(skill)
    skill_set = set(s)

    for tree in skill_trees:
        # print(tree)
        queue = []
        for i in range(len(tree)):
            if tree[i] in skill_set:
                queue.append(tree[i])
        user_skill = ''.join(queue)
        if user_skill in skill and skill.index(user_skill) == 0:
            answer += 1
    # print(answer)
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) # 2