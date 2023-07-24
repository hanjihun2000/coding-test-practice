def solution(park, routes):
    directions = {'E':[0,1], 'W':[0,-1], 'S':[1,0], 'N':[-1,0]}
    start_coord = []
    obstacle_coords = []
    for r, row in enumerate(park):
        for c, col in enumerate(row):
            if col == 'S':
                start_coord.append([r,c])
            if col == 'X':
                obstacle_coords.append([r,c])
    skip = False
    for step in routes:
        temp_coord = start_coord[0]
        # check if there is any obstacle or out of range
        for i in range(1, int(step[2]) + 1):
            move_coord = [x + y for x, y in zip(directions[step[0]], start_coord[0])]
            if move_coord in obstacle_coords:
                start_coord[0] = temp_coord
                skip = True
                break
            if (move_coord[0] < 0 or move_coord[0] > r) or (move_coord[1] < 0 or move_coord[1] > c):
                start_coord[0] = temp_coord
                skip = True
                break
            start_coord[0] = move_coord
        if skip is True:
            continue
    answer = start_coord[0]
    return answer