def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for who in callings:
        idx = result[who]
        result[who] = idx - 1
        result[players[idx - 1]] = idx
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
    return players