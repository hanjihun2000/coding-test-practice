def solution(board, moves):
    answer = 0
    res = []
    for i in moves:
        for r in board:
            if r[i-1] != 0:
                if len(res) != 0 and res[-1] == r[i-1]:
                    answer += 2
                    res = res[:-1]
                    r[i-1] = 0
                    break
                res.append(r[i-1])
                r[i-1] = 0
                break
    return answer