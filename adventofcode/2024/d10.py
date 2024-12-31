START_POINT = 0
END_POINT = 9
REQUIRED_LENGTH = 10
DIRECTIONS = [
    (-1, 0),  # curr_direction = 0, up
    (0, 1),  # curr_direction = 1, right
    (1, 0),  # curr_direction = 2, down
    (0, -1),  # curr_direction = 3, left
]


def is_in_map(map_ls: list[str], x: int, y: int):
    if not 0 <= x < len(map_ls):
        return False
    if not 0 <= y < len(map_ls[0]):
        return False
    return True


def walk_path(map_ls: list, x: int, y: int):
    pass


def get_path(map_ls, pos: tuple[int, int]):
    x, y  = pos
    path = [pos]
    curr_val = 0
    while True:
        path_found = False
        for move_x, move_y in DIRECTIONS:
            new_x, new_y = x + move_x, y + move_y
            if is_in_map(map_ls, new_x, new_y) and map_ls[new_x][new_y] == curr_val + 1:
                x, y = new_x, new_y
                curr_val += 1
                path.append((x, y))
                path_found = True
                break
        if not path_found:
            break
    return path


def get_path_ls(map_ls):
    path_set = set()
    for row_idx, r in enumerate(map_ls):
        for col_idx, c in enumerate(r):
            if c == START_POINT:
                path = get_path(map_ls, (row_idx, col_idx))
                target_path = (path[0], path[-1])
                if len(path) == REQUIRED_LENGTH:
                    path_set.add(target_path)
    return path_set


def get_q1_score(paths: list):
    # print(paths)
    path_dict = {}
    for start, end in paths:
        if start in path_dict:
            path_dict[start].append(end)
        else:
            path_dict[start] = [end]
    for k, v in path_dict.items():
        pass
        print(f"{k=}, {v=}")
    print(len(path_dict))
    # print(len(set()))
    return sum(i*len(j) for i, j in path_dict.items())


if __name__ == "__main__":
    with open("d10.txt") as f:
        content = f.readlines()
    content_raw = "".join(content)

    map_ = [list(map(int, list(i.strip()))) for i in content]
    # print(content)
    row = len(map_)
    col = len(map_[0])
    # print(row, col)

    # starting_pt = content_raw.count(str(START_POINT))
    # end_pt = content_raw.count(str(END_POINT))
    # print(starting_pt, end_pt)
    all_path = get_path_ls(map_)
    q1_score = get_q1_score(all_path)
    print(q1_score)
