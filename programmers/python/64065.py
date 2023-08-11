# 2019 카카오 개발자 겨울 인턴십 - 튜플
def solution(s):
    answer = []
    sep = s.split("},{")
    tuple_set = []
    for i in sep:
        i = i.strip("{}").split(",")
        tuple_set.append(i)
    tuple_set.sort(key=lambda x: len(x))
    for i in tuple_set:
        for j in range(len(i)):
            if int(i[j]) in answer:
                continue
            answer.append(int(i[j]))
    return answer
