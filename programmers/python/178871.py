def solution(players, callings):
    players_dict = {player:idx for idx, player in enumerate(players)}
    for calling in callings:
        front, calling_idx = players[players_dict[calling]-1], players_dict[calling]
        players_dict[calling], players[calling_idx] = players_dict[front], front
        players_dict[front], players[calling_idx-1] = calling_idx, calling
    return players
    
    # Takes too long due to the time complexity of index() method, O(n).
    # for calling in callings:
    #     calling_idx = players.index(calling)
    #     players[calling_idx] = players[calling_idx-1]
    #     players[calling_idx-1] = calling
    # return players
        