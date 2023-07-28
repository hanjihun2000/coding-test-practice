# 하노이의 탑
def towerOfHanoi(n, start, des, aux, answer):
    if n == 1:
        return answer.append([start, des])
    towerOfHanoi(n-1, start, aux, des, answer)
    answer.append([start, des])
    towerOfHanoi(n-1, aux, des, start, answer)

def solution(n):
    answer = []
    towerOfHanoi(n, 1, 3, 2, answer)
    return answer