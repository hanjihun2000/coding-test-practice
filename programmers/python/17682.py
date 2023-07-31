import math
import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    options = {'*': 2, '#': -1}
    scores = []
    dartResult = re.findall('[0-9]+[SDT][*#]?', dartResult)
    for i, s in enumerate(dartResult):
        num = int(re.findall('[0-9]+', s)[0])
        power = bonus[re.findall('[SDT]', s)[0]]
        num = pow(num, power)
        op = re.findall('[*#]', s)
        if op:
            num *= options[op[0]]
            if op[0] == '*' and i-1 >= 0:
                scores[i-1] *= options[op[0]]
        scores.append(num)  
    answer = scores[0] + scores[1] + scores[2]
    return answer