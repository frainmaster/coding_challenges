from functools import lru_cache
import time


def flatten_ls(ls: list):
    ans_ls = []

    def flatten(elem):
        if isinstance(elem, int):
            ans_ls.append(elem)
        elif isinstance(elem, list):
            for item in elem:
                flatten(item)

    flatten(ls)
    return ans_ls


@lru_cache(maxsize=None)
def transform_stone(num: int, iter_cnt=0) -> list[int]:
    num_str = str(num)
    if num == 0:
        ans = [1]
    elif len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        num1, num2 = num_str[:mid], num_str[mid:]
        ans = [int(num1), int(num2)]
    else:
        ans = [num * 2024]
    if iter_cnt == 0:
        return ans
    else:
        return flatten_ls([transform_stone(i, iter_cnt-1) for i in ans])


def process_stones(stone_str: str, curr_iter=0, target_iter=5):
    stones = stone_str.split()
    new_stone_ls = []
    for stone in stones:
        # new_stone_ls.extend(transform_stone(int(stone), iter_cnt=target_iter-curr_iter))  # did not work
        new_stone_ls.extend(transform_stone(int(stone)))
    new_stone_str = " ".join(map(str, new_stone_ls))
    return new_stone_str


def blink(stone_str: str, n=5):
    print("start", stone_str)
    for i in range(n):
        stone_str = process_stones(stone_str, curr_iter=i, target_iter=n)
        print(i, stone_str)
    return stone_str


if __name__ == "__main__":
    with open("d11.txt") as f:
        content = f.read()
    content = content.strip()

    start = time.time()
    stone_ans = blink(content, n=20)
    # print(stone_ans)
    stone_cnt = stone_ans.split()
    print(len(stone_cnt))
    end = time.time()
    print(f"time taken: {end - start:.2f}")
