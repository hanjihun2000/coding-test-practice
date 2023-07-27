# 2020 카카오 인턴십 키패드 누르기
num_dict = {str(i):((i - 1) // 3, (i - 1) % 3) for i in range(1, 10)}

def calculate_distance(pos, target):
    distance = abs(num_dict[target][0] - num_dict[pos][0]) + abs(num_dict[target][1] - num_dict[pos][1])
    return distance

def solution(numbers, hand):
    answer = ''
    # special cases
    num_dict['*'] = (3, 0)
    num_dict['0'] = (3, 1)
    num_dict['#'] = (3, 2)
    l_only = ['1', '4', '7']
    r_only = ['3', '6', '9']
    l_pos = '*'
    r_pos = '#'
    hand_used = ''
    for number in numbers:
        number = str(number)
        if number in l_only:
            l_pos = number
            hand_used = 'L'
            answer += hand_used
            continue
        if number in r_only:
            r_pos = number
            hand_used = 'R'
            answer += hand_used
            continue
        l_distance = calculate_distance(l_pos, number)
        r_distance = calculate_distance(r_pos, number)
        if l_distance == r_distance:
            if hand == "left":
                l_pos = number
                hand_used = 'L'
                answer += hand_used
                continue
            if hand == "right":
                r_pos = number
                hand_used = 'R'
                answer += hand_used
                continue
        if l_distance > r_distance:
            r_pos = number
            hand_used = 'R'
            answer += hand_used
            continue
        l_pos = number
        hand_used = 'L'
        answer += hand_used   
    return answer