# https://adventofcode.com/2024/day/3 q2
import re

with open('d03.txt') as f:
    content = f.readlines()

def mul(a, b):
    return a * b

do = r"do\(\)"
dont = r"don't\(\)"
pattern = r"mul\(\d+,\d+\)"


def get_matches(n: str):
    ptn = re.finditer(pattern, n)
    dos = re.finditer(do, n)
    donts = re.finditer(dont, n)
    get = True
    all_words = list(ptn) + list(dos) + list(donts)
    all_words = sorted(all_words, key=lambda x: x.start())
    take = []
    for i in all_words:
        word = i.group()
        if word == "don't()":
            get = False
        elif word == "do()":
            get = True
        else:
            if get:
                take.append(word)
    return take


if __name__ == "__main__":
    total = 0
    content_combined = ""
    for i in content:
        content_combined += i
    content_combined = [content_combined]
    for i in content_combined:
        ans = get_matches(i)
        ans = [i.replace("mul(", "").replace(")", "").split(",") for i in ans]
        ans = [[int(i[0]), int(i[1])] for i in ans]
        mul_ans = [mul(*i) for i in ans]
        # print(mul_ans)
        # print(sum(mul_ans))
        total += sum(mul_ans)
    print(total)
