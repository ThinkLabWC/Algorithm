def solution(bandage, health, attacks):
    answer = 0

    time = attacks[0][0]
    attack_dict = {}
    for attack in attacks:
       attack_dict[attack[0]] = attack[1]
       if time < attack[0]:
           time = attack[0]
           
    # time_queue = [None] * time
    h = health
    seq = 0
    for i in range(0, time + 1):
        if attack_dict.get(i):
            h = max(h - attack_dict[i], 0)
            seq = 0
        else:
            if h < health :
                h = min(h + bandage[1], health)
                seq += 1
            if seq == bandage[0]:
                h = min(h + bandage[2], health)
                seq = 0
        # print(i, h, seq)
        if h <= 0:
            break
            
    answer = -1 if h <= 0 else h
    print(answer)
    return answer

# solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]) # 5
# # solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]) # -1
# solution([1, 1, 1], 5, [[1, 2], [3, 2]]) # 3

# solution([1, 100, 1], 5, [[1, 10], [3, 2]]) # -1
solution([1, 1, 1], 5, [[1, 1], [2, 1], [3, 1], [4, 1]]) # 
		