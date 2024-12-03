import re

input = ""
with open("3.txt") as f:
    input = f.read()


def multiply_parse(input):
    regex = r"mul\((\d+),(\d+)\)"
    # search = re.findall(regex, input)
    total_sum = 0
    for match in re.finditer(regex, input):
        a, b = match.groups()
        total_sum += int(a) * int(b)
    return total_sum


def conditional_parse(input):
    regex = r"(mul)\((\d+),(\d+)\)|(do)\(|(don't)\("
    mult = True
    total_sum = 0
    for match in re.finditer(regex, input):
        data = match.groups()
        if data[4] == "don't":
            mult = False
        if data[3] == "do":
            mult = True
        elif mult:
            total_sum += int(data[1]) * int(data[2])
    return total_sum



result = print(multiply_parse(input))
result = print(conditional_parse(input))