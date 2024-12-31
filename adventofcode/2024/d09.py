EMPTY_SPACE = "."


def prepare_ls(long_str: str):
    processed_ls = []
    for idx, char in enumerate(long_str):
        if idx % 2 == 0:
            processed_ls += [str(idx // 2)] * int(char)
        else:
            processed_ls += [EMPTY_SPACE] * int(char)
    return processed_ls


def move_blocks(processed_ls: list):
    empty_space_cnt = processed_ls.count(EMPTY_SPACE)
    print(f"before {empty_space_cnt=}")
    block_ls = [i for i in processed_ls]
    idx = 0
    while empty_space_cnt > 0:
        if block_ls[idx] == EMPTY_SPACE:
            char = ""
            while True:
                if block_ls[-1] != EMPTY_SPACE:
                    char = block_ls.pop()
                    break
                else:
                    empty_space_cnt -= 1
                    block_ls.pop()
            try:
                if char == "":
                    print("wrong 2")
                block_ls[idx] = char
                empty_space_cnt -= 1
            except IndexError:
                print(f'wrong, {idx=}, {len(block_ls)=}')
                pass
        idx += 1
    print(f"after {empty_space_cnt=}")
    return block_ls


def get_checksum_score(block_ls: list):
    return sum([idx * int(i) for idx, i in enumerate(block_ls)])


if __name__ == "__main__":
    with open("d09.txt") as f:
        content = f.read()
    content = content.strip()

    # print(len(content))

    processed_ls = prepare_ls(content)

    processed_blocks = move_blocks(processed_ls)

    # get checksum value
    product_sum = get_checksum_score(processed_blocks)
    print(product_sum)
    # print(processed_blocks[-10:])

    # test
    test_str = "2333133121414131402"
    test_ls = prepare_ls(test_str)
    print(test_ls)
    test_block = move_blocks(test_ls)
    test_ans = get_checksum_score(test_block)
    print(f"{test_ans=}")

