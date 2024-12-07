from itertools import product


def get_data():
    with open("7.txt") as f:
        for line in f:
            yield line.strip()


def is_calibrated(inp, res):
    for ops in product(["*", "+"], repeat=len(inp) - 1):
        exp = str(inp[0])
        val = 0
        for o in range(len(ops)):
            exp += f"{ops[o]}{inp[o+1]}"
            val = str(eval(exp))
            exp = val
        if int(val) == res:
            return True
    return False


def elephant_hidden(inp, res):
    for ops in product(["*", "+", "||"], repeat=len(inp) - 1):
        exp = str(inp[0])
        val = 0
        for o in range(len(ops)):
            if ops[o] == "||":
                exp += f"{inp[o + 1]}"
            else:
                exp += f"{ops[o]}{inp[o+1]}"
            val = str(eval(exp))
            exp = val
        if int(val) == res:
            return True
    return False


cal_result = 0
for data in get_data():
    res, inp = data.split(":")
    inp = list(map(int, inp.split()))
    res = int(res)
    # Part 1
    # if is_calibrated(inp, res):
    #     cal_result = int(cal_result + res)
    # Part 2
    # if elephant_hidden(inp, res):
    #     cal_result = int(cal_result + res)

print(cal_result)
