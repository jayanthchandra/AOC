from collections import defaultdict

def build_grid(arr):
    grid = defaultdict()
    for row, line in enumerate(arr)
        for col, val in enumerate(arr):
            grid[(row, col)] = val
    return grid
# part 1
def ceres_search(grid, word):
    direction = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (1,1),
        (-1,1),
        (1, -1)
    ]
    count = 0
    for pos, val in grid.items():
        if val == word[0]:
            x, y = pos
            for dx, dy in direction:
                r, c = x, y
                is_valid = True
                for char in word[1:]:
                    r += dx
                    c += dy
                    letter = grid.get((r, c))
                    if letter is None or letter != char:
                        is_valid = False
                        break
                if is_valid:
                    count += 1
    return count 
#part 2
def ceres_xsearch(grid):
    direction =  [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    count = 0
    for pos, val in grid.items():
        if val == 'A':
            x, y = pos
            left_diag = [grid.get((x + dx, y + dy)) for dx, dy in direction[0:2]]
            right_diag = [grid.get((x + dx, y + dy)) for dx, dy in direction[2:]]]
            is_valid = False
            if (
                "M" in left_word
                and "S" in left_word
                and "M" in right_word
                and "S" in right_word
            ):
                count += 1
    return count

input = open("4.txt").read().split("\n")
arr = build_grid(input)
# part 1
print(ceres_search(arr, word))
# part 2
print(ceres_mas_search(arr))

# Invoke pytest 4.py -v 
def test_part1():
    arr = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    word_search = build_grid(arr)
    word = "XMAS"
    assert ceres_search(word_search, word) == 18

def test_part2():
    arr = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    word_search = build_grid(arr)
    assert ceres_xsearch(word_search) == 9


                    