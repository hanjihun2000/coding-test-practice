# 기사단원의 무기
from math import sqrt
from functools import reduce

def solution(number, limit, power):
    num_factors = []
    for i in range(1, number+1):
        step = 2 if i % 2 else 1
        num = len(set(reduce(list.__add__, ([j, i // j] for j in range(1, int(sqrt(i))+1, step) if i % j == 0))))
        if num > limit:
            num_factors.append(power)
        else:
            num_factors.append(num)
    answer = sum(num_factors)
    return answer