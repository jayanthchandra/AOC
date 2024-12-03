import polars as pl

df = pl.read_csv("2.txt", separator=' ', has_header=False)
df.head()

def check_logic(row):
  inc = dec = True
  for i in range(len(row)-1):
    if row[i] == None or row[i+1] == None:
      continue
    diff = abs(row[i] - row[i+1])
    if diff > 3 or diff < 1:
      return False
    if row[i] > row[i+1]:
      inc = False
    else:
      dec = False
 return inc or dec 

diff = df.map_rows(check_logic)

# Part 2
def brute_force(row):
    def is_monotonic(row):
        inc = dec = True
        for i in range(len(row) - 1):
            if row[i] == None or row[i+1] == None:
                continue
            if row[i] > row[i+1]:
                inc = False
            else:
                dec = False
        return inc or dec

    def is_valid_diff(row):
        for i in range(len(row)-1):
            if row[i] == None or row[i+1] == None:
                continue
            diff = abs(row[i] - row[i+1])
            if diff < 1 or diff > 3:
                return False
        return True

    if is_monotonic(row) and is_valid_diff(row):
        return True

    for i in range(len(row)):
        if row[i] == None:
            continue
        new_row = row[:i] + row[i+1:]
        print(new_row)
        if is_monotonic(new_row) and is_valid_diff(new_row):
            return True
    return False

correction_difference = df.map_rows(brute_force)
correction_difference
