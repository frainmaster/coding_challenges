with open("d06.txt") as f:
    MAP = f.readlines()

MAP = [list(i.strip()) for i in MAP]
BLOCKER = "#"
STARTING_POINT = "^"
BOMB_CNT = sum([i.count("#") for i in MAP])
DIRECTIONS = [
    (-1, 0),  # curr_direction = 0, up
    (0, 1),  # curr_direction = 1, right
    (1, 0),  # curr_direction = 2, down
    (0, -1),  # curr_direction = 3, left
]
curr_direction = 0
COOR = (0, 0)

# find starting point
for i in range(len(MAP)):
    found = False
    for j in range(len(MAP[0])):
        if MAP[i][j] == STARTING_POINT:
            COOR = (i, j)
            found = True
            break
    if found:
        break


def is_in_map(map_ls: list[str], x: int, y: int):
    if not 0 <= x < len(map_ls):
        return False
    if not 0 <= y < len(map_ls[0]):
        return False
    return True


def move(x, y, dx, dy) -> tuple:
    return (x + dx, y + dy)


def turn_right(n):
    if n not in range(4):
        raise ValueError(f"direction not 0123: {n}")
    if n == 3:
        return 0
    return n + 1


def begin_walking_and_write_path(map_ls: list[list[str]], moving_coor: tuple, direction: int):
    path = [moving_coor]
    new_map = [list(i) for i in map_ls]
    while is_in_map(map_ls, *moving_coor):
        new_x, new_y = move(*moving_coor, *DIRECTIONS[direction])
        if not is_in_map(map_ls, new_x, new_y):  # exit the map
            break
        elif map_ls[new_x][new_y] == BLOCKER:  # hit a blocker
            direction = turn_right(direction)
            # write path to new map
            if new_map[moving_coor[0]][moving_coor[1]] != STARTING_POINT:
                new_map[moving_coor[0]][moving_coor[1]] = "+"
        else:  # can walk
            moving_coor = new_x, new_y
            path.append(moving_coor)
            if new_map[new_x][new_y] == STARTING_POINT:
                continue
            if (curr_char := new_map[new_x][new_y]) == ".":
                if direction == 0:
                    new_map[moving_coor[0]][moving_coor[1]] = "↑"
                elif direction == 1:
                    new_map[moving_coor[0]][moving_coor[1]] = ">"
                elif direction == 2:
                    new_map[moving_coor[0]][moving_coor[1]] = "↓"
                elif direction == 3:
                    new_map[moving_coor[0]][moving_coor[1]] = "<"
            elif curr_char in "↑>↓<" and direction in [0, 2]:
                new_map[moving_coor[0]][moving_coor[1]] = "+"
            elif curr_char in "↑>↓<" and direction in [1, 3]:
                new_map[moving_coor[0]][moving_coor[1]] = "+"
    return path, new_map


def update_map_with_new_blocker(map_ls: list[list[str]], x: int, y: int):
    map_cp = [list(i) for i in map_ls]
    map_cp[x][y] = "#"
    return map_cp


def check_if_path_is_trapped(map_ls: list[list[str]], moving_coor: tuple, direction: int):
    max_repetition = 5
    path = {moving_coor: 0}
    while is_in_map(map_ls, *moving_coor):
        new_x, new_y = move(*moving_coor, *DIRECTIONS[direction])
        if not is_in_map(map_ls, new_x, new_y):  # exit the map
            break
        elif map_ls[new_x][new_y] == BLOCKER:  # hit a blocker
            direction = turn_right(direction)
        else:  # can walk
            moving_coor = new_x, new_y
            if moving_coor in path:
                path[moving_coor] += 1
            else:
                path[moving_coor] = 1
        if max_repetition in path.values():
            return True
    return False


if __name__ == "__main__":
    # q1
    path, _new_map = begin_walking_and_write_path(MAP, COOR, curr_direction)

    # print(path)
    print(len(set(path)))

    # # make new map
    # with open("d06_new.txt", "w") as f:
    #     for line in _new_map:
    #         f.write("".join(line) + "\n")

    # q2: brute force
    total_checks = len(MAP) * len(MAP[0]) - BOMB_CNT
    check_cnt = 0
    trapped_path = 0
    err_ls = []
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == ".":
                temp_map = update_map_with_new_blocker(MAP, i, j)
                check_cnt += 1
                try:
                    result = check_if_path_is_trapped(temp_map, COOR, curr_direction)
                    if result:
                        trapped_path += 1
                    print(f"check count {check_cnt}/{total_checks} ({i},{j}): {result}")
                except Exception as e:
                    err_ls.append((i, j))
                    print(f"check count {check_cnt}/{total_checks} ({i},{j}): error - {e}")

    print(trapped_path)
