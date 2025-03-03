def movePlayer(rankByPlayerDic, playerByRankDic, callingPlayer):
    rank = playerByRankDic[callingPlayer]

    newRank = rank - 1
    curPlayer = rankByPlayerDic[newRank]
    rankByPlayerDic[rank] = curPlayer
    rankByPlayerDic[newRank] = callingPlayer

    playerByRankDic[callingPlayer] = newRank
    playerByRankDic[curPlayer] = rank
    return 

def solution(players, callings):
    answer = []
    rankByPlayerDic = { index: value for index, value in enumerate(players) }
    playerByRankDic = { value: index for index, value in enumerate(players) }
    for i in range(0, len(callings)):
        movePlayer(rankByPlayerDic, playerByRankDic, callings[i])
    # print(rankByPlayerDic)
    # print(playerByRankDic)
    answer = list(rankByPlayerDic.values())
    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
# ["mumu", "kai", "mine", "soe", "poe"]