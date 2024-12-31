from math import prod
from itertools import product


def sum_(a, b):
    return a + b


def mul_(a, b):
    return a * b


def conc(a, b):  # concatenate
    ans = str(a) + str(b)
    return int(ans)


if __name__ == "__main__":
    with open("d07.txt") as f:
        content = f.readlines()

    ls = [i.split(":") for i in content]
    ls = [[int(i[0]), list(map(int, i[1].strip().split()))] for i in ls]

    # q1
    correct_total = 0
    for target, int_ls in ls:
        correct = False
        for funcs in product([sum_, mul_], repeat=len(int_ls)-1):
            calc = int_ls[0]
            for idx, func in enumerate(funcs):
                calc = func(calc, int_ls[idx+1])
            if calc == target:
                correct_total += target
                break
    print(correct_total)

    # q2
    correct_total = 0
    for target, int_ls in ls:
        correct = False
        for funcs in product([sum_, mul_, conc], repeat=len(int_ls)-1):
            calc = int_ls[0]
            for idx, func in enumerate(funcs):
                calc = func(calc, int_ls[idx+1])
            if calc == target:
                correct_total += target
                break
    print(correct_total)
