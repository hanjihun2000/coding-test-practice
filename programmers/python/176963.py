def solution(name, yearning, photo):
    name_yearning_dict = {n : y for n, y in zip(name, yearning)}   
    answer = []
    for names in photo:
        score = 0
        for name in names:
            if name in name_yearning_dict:
                score += name_yearning_dict[name]
        answer.append(score)
    return answer