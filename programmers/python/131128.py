# 숫자 짝궁
from collections import Counter
def solution(X, Y):
    answer = ''
    common = []
    X_count = Counter(X)
    Y_count = Counter(Y)
    for i in range(10):
        X_num = X_count[str(i)]
        Y_num = Y_count[str(i)]
        if X_num != 0 and Y_num != 0:
            common.append(str(i) * X_num) if X_num < Y_num else common.append(str(i) * Y_num)
    common = sorted(common, key=lambda x: x[0], reverse=True)
    if common == []:
        return "-1"
    elif common[0][0] == '0':
        return "0"
    else:
        for i in common:
            answer += i
    return answer

# --- Best solution done by others
def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer