rules = {}
pages = []

with open("5.txt") as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            a, b = line.split("|")
            if a in rules:
                rules[a].append(b)
            else:
                rules[a] = [b]
        else:
            pages.append(line.split(","))


def is_order(update, rules):
    for i in range(1, len(update)):
        for j in range(i + 1, len(update)):
            rule = rules.get(update[j], [])  # check the next element
            if (
                update[i] in rule
            ):  # check if number is present in this list then it is wrong
                return 0
    return int(update[len(update) // 2])


def correct_order(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            rule = rules.get(update[j], [])  # check the next element
            if (
                update[i] in rule
            ):  # check if number is present in this list then it is wrong
                update[i], update[j] = update[j], update[i]
                return correct_order(update, rules)
    return int(update[len(update) // 2])


pages = pages[1:]
part_1 = 0
part_2 = 0
for page in pages:
    part_1 += is_order(page, rules)
    part_2 += correct_order(page, rules)

print(part_1)
print(part_2 - part_1)
