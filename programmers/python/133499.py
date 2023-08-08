# 옹알이 (2)
import re

def solution(babbling):
    answer = 0
    for word in babbling:
        prev = ""
        while word != "":
            match = re.search("^(aya|ye|woo|ma)", word)
            if match is None or prev == word[match.span()[0]:match.span()[1]]:
                break
            prev = word[match.span()[0]:match.span()[1]]
            word = word[match.span()[1]:]
        if word == "":
            answer += 1
    return answer