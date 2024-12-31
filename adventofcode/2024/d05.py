import sys

with open("d05.txt") as f:
    content = f.readlines()

content = [i.strip() for i in content]
space = content.index("")

rules = content[:space]
updates = content[space+1:]

updates = [i.split(",") for i in updates]

# q1
def get_valid_updates(n: list[str], rule: list[str]):
    target_rule = [i for i in rule if any(j in i for j in n)]
    target_rule = [i.split("|") for i in target_rule]
    target_rule = [i for i in target_rule if all(j in n for j in i)]
    for (a, b) in target_rule:
        if n.index(b) < n.index(a):
            return 0
    return int(n[len(n)//2])

# q2
def fix_wrong_updates(updates: list[str], rule: list[str]):
    valid = True
    target_rule = [i for i in rule if any(j in i for j in updates)]
    target_rule = [i.split("|") for i in target_rule]
    target_rule = [i for i in target_rule if all(j in updates for j in i)]
    for (a, b) in target_rule:
        if updates.index(b) < updates.index(a):
            valid = False
    if valid:
        return 0
    # sort by getting score
    scores = {i: 0 for i in updates}
    for (a, b) in target_rule:
        scores[a] += 1
    sorted_list = sorted(scores, key=lambda x: scores[x])
    return int(sorted_list[len(updates)//2])


if __name__ == "__main__":
    if not sys.argv[1:] or sys.argv[1] == "1":
        ans = 0
        for i in updates:
            ans += get_valid_updates(i, rules)
        print(ans)

    else:
        ans = 0
        for i in updates:
            ans += fix_wrong_updates(i, rules)
        print(ans)
