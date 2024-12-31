from collections import Counter
from itertools import combinations


def is_in_map(map_ls: list[list[str]], x: int, y: int):
    if not 0 <= x < len(map_ls):
        return False
    if not 0 <= y < len(map_ls[0]):
        return False
    return True


def get_char_coor(map_ls: list[list[str]], char: str):
    coor_ls = []
    for x, i in enumerate(map_ls):
        for y, j in enumerate(i):
            if j == char:
                coor_ls.append((x, y))
    return coor_ls


def get_antinodes_loc_q1(map_ls: list[list[str]], pos1: tuple, pos2: tuple):
    x_diff = pos2[0] - pos1[0]
    y_diff = pos2[1] - pos1[1]
    antinodes_pair = []
    if is_in_map(map_ls, (n1_0 := pos1[0]-x_diff), (n1_1 := pos1[1]-y_diff)):
        antinodes_pair.append((n1_0, n1_1))
    if is_in_map(map_ls, (n2_0 := pos2[0]+x_diff), (n2_1 := pos2[1]+y_diff)):
        antinodes_pair.append((n2_0, n2_1))
    return antinodes_pair


def get_antinodes_loc_q2(map_ls: list[list[str]], pos1: tuple, pos2: tuple):
    x_diff = pos2[0] - pos1[0]
    y_diff = pos2[1] - pos1[1]
    antinodes_pair = [pos1, pos2]
    n1_0 = pos1[0]
    n1_1 = pos1[1]
    while True:
        n1_0 -= x_diff
        n1_1 -= y_diff
        if is_in_map(map_ls, n1_0, n1_1):
            antinodes_pair.append((n1_0, n1_1))
        else:
            break
    n2_0 = pos2[0]
    n2_1 = pos2[1]
    while True:
        n2_0 += x_diff
        n2_1 += y_diff
        if is_in_map(map_ls, n2_0, n2_1):
            antinodes_pair.append((n2_0, n2_1))
        else:
            break
    return antinodes_pair


if __name__ == "__main__":
    with open("d08.txt") as f:
        content = f.readlines()
    content = [i.strip() for i in content]
    map_ = [list(i) for i in content]

    all_chars = "".join(content).replace(".", "")
    all_unique_chars = set(all_chars)
    char_cnt = Counter(all_chars)
    # print(char_cnt)

    antinodes_ls_q1 = []  # q1
    antinodes_ls_q2 = []  # q2
    for char in all_chars:
        chars_coor = get_char_coor(map_, char)
        pairs = list(combinations(chars_coor, 2)) # make pairs
        for pair in pairs:
            antinodes_q1 = get_antinodes_loc_q1(map_, *pair)
            antinodes_ls_q1.extend(antinodes_q1)
            antinodes_q2 = get_antinodes_loc_q2(map_, *pair)
            antinodes_ls_q2.extend(antinodes_q2)
    # print(len(antinodes_ls_q1))
    print(len(set(antinodes_ls_q1)))
    # print(len(antinodes_ls_q2))
    print(len(set(antinodes_ls_q2)))
