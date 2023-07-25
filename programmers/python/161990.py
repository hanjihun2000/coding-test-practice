def solution(wallpaper):
    file_coords = []
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                file_coords.append([i,j])
    r = [idx[0] for idx in file_coords]
    c = [idx[1] for idx in file_coords]
    min_r, max_r = min(r), max(r)
    min_c, max_c = min(c), max(c)
    answer = [min_r, min_c, max_r+1, max_c+1]
    return answer