# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외
def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0
    lotto_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    }
    for i in range(0, len(lottos)):
        print(lottos[i], win_nums, count, zero_count,)
        if lottos[i] in win_nums:
            count += 1
        if lottos[i] == 0:
            zero_count += 1
    answer = [lotto_dict[count + zero_count], lotto_dict[count]]
    return answer

# solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) # [3, 5]
# solution([0,0,0,0,0,0], [38, 19, 20, 40, 15, 25]) # [1, 6]
# solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) # [1, 1]